import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #To check whether this username already exists in databse
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Sorry, this username is taken. Please try again with a new username!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #To add the new user's username into session cookie using session imported from flask
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #To check whether the username entered by the user is already in the database
        already_a_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if already_a_user:
            #To check whether the user's input matches the hashed password
            if check_password_hash(already_a_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                #For if the user's input does not match the password in the database for the supplied username
                flash("Incorrect Username and Password combination. Please try again!")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and Password combination. Please try again!")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    #Collect session user's name from the database
    username = mongo.db.users.find_one({"username": session["user"]})["username"]


    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # To remove the user from the session cookies
    flash("You have been logged out. See you again soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe")
def add_recipe():
    cooking_methods = mongo.db.cooking_methods.find().sort("cooking_method_name", 1)
    diff_levels = mongo.db.diff_levels.find().sort("diff_level", 1)
    return render_template("add_recipe.html", cooking_methods=cooking_methods, diff_levels=diff_levels)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
