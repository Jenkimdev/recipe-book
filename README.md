# [Recipe Hub]()   

<img src="/static/img/hero_wf.png" alt="mockup_of_homepage" target="_blank" rel="noopener" width="800">

"Recipe Hub" - Python and Data-Centric Development Milestone Project.

The main purpose of this full-stack MongoDB-based Flask project is to create a database of recipes that allows users to create, read, update and delete (CRUD) any recipes.
"Recipe Hub" gives full access to all recipe content withinin the database for non-registered users. At the same time, it gives the opportunity to create an account and benifit from having seemless access to all features of the website.
Registered users can add new recipes, edit and delete their own previously added recipes. 

[Recipe Hub]() is a simple way to browse, create and store all intersting recipes!   
Sign and be on your way to seemless recipe storage and organisation. Why not contribute, cook and enjoy?

---

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Technologies Used](#technologies-used)

4. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Validators](#validators)
    - [Compatibility and Responsiveness](#compatibility-and-responsiveness)

5. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

---

## UX
My main goal with regards to UX was to build a database and website that was minimalistic in design, simple to use and also where users can create, view and update any recipes of their own, as well as view any recipes created by others. The main target audience for this web application would be anybody who has passion for cooking and would like to discover new recipes, as well as those who need a simple and convenient way to store their recipes. I have implemented a fun, but modern, colourful and user-friendly interface with easy methods access to all information. This is the key to giving users ease of reliability, security and confidence in the service. 
With this in mind, I developed the web app in a way that allowed everybody to view the recipe database, the moment they access the app. However, I thought it best that only authors can make changes to their own recipes.   


### User Stories
**As a user, I want/expect to:**
- be able to view any information relating to all recipes in the database, without having to register
- have access to all information required to effectively recreate the recipe. For example cooking times, ingredtients etc.
- be able to browse through a catelogue of all recipes if needed
- be able to register for security
- be able to to add new recipes 
- be able to edit my own recipes that are stored securely within the database
- be able to delete any of my own recipes at any time, should the need arise.
- be able to easily and securely log out any time and have the session terminated
- be able to use the website from any reasonable device, for example laptop, tablets and a smartphone.

### Design
My goal when considering design was to create a fun and colourful website that is overall user friendly, but also has a modern feel with emphasis on providing information about recipes in a readable and eye-catching way. Therefore, following design choices were made:
#### Framework
[Materialize](https://materializecss.com/), front-end framework based on Material Design was chosen for this project for its modern interface and ease of use. It was used for creating features such as navbar, cards, forms, as well as for its grid.  
[JQuery](https://jquery.com/) was used for initializing some Materialize elements listed above, as well as for custom functions, simple DOM manipulation.
#### Colour Scheme
One of the main goals was to focus user's attention on the recipe cards and recipe images. Therefore, I decided to opt for a lot of whitespace and mostly white background accross the website, giving preferences to calm white and grey colours. In order to brighten things up, I also added color in the form of making most of the colour scheme based froma. teal pallete, which I know can be overwhelming, but I felt users would appreciate this energy. 
I have routineley used different shades of the same colour accross the web app. The primary colour used for main buttons and headings is teal as it seems to create a nice contrast with light and white backgrounds. The secondary colour used for icons, dividers and some other buttons is red for any urgency related element, for example in the delete function.   

#### Typography
I gave some thought to whether I should implement an external library for any fonts or typography within this project, but I felt that the web app was strictly about being functional and easy to use, so with this in mind, I opted for one or two simply, easy to ready built in fonts instead. 

#### Icons
Icons are used widely, as they are good attention grabbers. They help users to find and scan content. Another advantage of using them is for ease of language and communication. They create more user-friendly experience for users, particularly those with any language challenges.  
I used [FontAwesome](https://fontawesome.com/) as the main icon library across the project (e.g. for navbar, forms, recipe details page). However,  [Materialize icons](https://materializecss.com/icons.html) were considered as well in some areas of the project.
#### Further styling decisions
- The recipe accordion was styled using the customer materialize classes, which I thought was verry effective and eye catching.

### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) was used to create all wireframes for the project as seen below:

![](/static/img/home_pre_login_wf.png)
![](/static/img/home_post_login_wf.png)
![](/static/img/register_wf.png)
![](/static/img/login_wf.png)
![](/static/img/profile.wf.png)
![](/static/img/add_recipe_wf.png)
![](/static/img/add_recipe_wf.png)

Initial wireframes may vary slightly from the finished project, as the development throughout this project was significant.

---

## Features
### Existing Features
#### Navbar   

![](/static/img/)

The navbar can slide up past the top of the page and is not fixed, this allows a user to easily navigate throughout the website with enough real estate. The logo is located in the top left corner on a desktop and on smaller devices. It redirects the user to the home page when clicked.
On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.     

For **non-logged in** users or **guests** navbar contains the following links:
![](/static/img/)
- Home
- Login
- Register    
   
For **logged-in** users, the navbar contains the following links:
![](/static/img/)
- Home
- New Recipe 
- Profile
- Logout

#### Home page featuring all Recipes   
The home page contains all recipes It also displays a functional search bar at the top of the screen. 

#### Browse All Recipes   
 ![](/static/img/)=

#### Register   
![](/static/img/)
The registration page allows a user to create a new account. The user is asked to fill the fields "username", "password".
When adding a username, the code compares it against existing usernames to ensure that it is unique. A username is also checked against validation, in the form of pattern attributes. If the user's input does not meet requirements, flash messages will inform a user about the error.
When the form is submitted successfully, a user is redirected to the home page and informed that account was created.
There is also a link to the login page for existing users at the bottom of the form.

#### Login   
![](/static/img/)
The login page features the form with "username" and "password" fields, allowing registered users to log into their account.
If the entered username and hashed password match the ones in the database, a user is redirected to the home page and informed that the  log in was successful. Otherwise, flash messages will be displayed about incorrect user's input.
There is also a link to the register page for new users at the bottom of the form.

#### Logout 
Hitting "logout" button if you are a logged in eser, ends your session and redirects you to the homepage.


#### Edit Recipe
The edit recipe page allows the logged in user to update information about the recipe. The "Edit" button will appear only for the author of the recipe when they are on the recipes paage and one of their own recipes is available.

As well as that, the defensive design (against brute-forcing) in place allows only author of the recipe to make changes. 
The form is pre-populated with the original recipe's details. After clicking "Edit recipe" button, the recipe is updated in the database and a user is redirected home and informed of the updated recipe.   
There is also a button "Cancel" that simply redirects a user to the home page to avoid having to resubmit form when clicking the back button.

#### Delete Recipe
The delete recipe function allows only author of the recipe to delete it. After a user clicks the "delete" button on one of the recipes on the recipes bage,  the recipe is deleted immediately. 
If so, upon clicking "delete" button the recipe will be removed from the database as well as from the "user_recipes" field of the recipe's author in "users" collection.

#### Profile Page   
![](/static/img/)
The profile page contains username and a brief personalised welcome message, but it also displays a message, regarding the development is currently undergoing, as some funtionaility is a work in progress.

### Features Left to Implement
There are some features that I considered were of secondary importance and I have not implemented them yet due to time constraints, but would like to do so in future.
#### Change Username and Password Functionality
At this stage I didn't consider this of paramount importance and thought it better, with the limited time I have had to complete the project, that I concentrate on the items in the marking critera. 
#### My favourites
User would have an opportunity to "like" other recipes, saving them in "my favourites" collection, which would be displayed on a separate page or on the profile page.
Each accordion card will include a small "heart" or "thumbs up" icon, which upon being selected will enable user to add the selected recipe to a "favourites" group..

---

## Technologies Used

- [GitPod](https://www.gitpod.io/) - IDE for developing this project.
- [Git](https://git-scm.com/) - version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.

### Front-End
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - to build the foundation of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - to create custom styles.

### Back-End
- [Python 3.8.2](https://www.python.org/) -  back-end programming language used for this project.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) - microframework for building and rendering web app pages.
- [MongoDB Atlas](https://www.mongodb.com/) - NoSQL database for storing back-end data.
- [PyMongo](https://api.mongodb.com/python/current/) - for Python to access the MongoDB database.
- [Werkzeug 0.16.1](https://werkzeug.palletsprojects.com/en/0.16.x/) - to generate and verify password hash and unhash functions.
- [Jinja 2.10.1](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML and implement template. inheritance.
- [Heroku](https://heroku.com/) - to host the project.

### Libraries
- [Materialize 1.0.0](https://materializecss.com/) - main responsive modern front-end framework used for grid and responsivesness.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project.
- [JQuery 3.5.0](https://jquery.com/) - to simplify DOM manipulation and to initialize Materialize functions.
---

## Testing
### Manual Testing 
#### User stories testing
All the following manual testing was implemented on both desktop and mobile devices.

##### All recipes and single recipe display
When I clicked  on "Home" page, I could see the recipe accordian cards are not functioning as expected.
I eventually concluded, that I had forgotten to initialise the accordion within the script file using jquery.

##### Create a new user account
I created my main account, as well as a few test accounts to test this functionality. Clicking on the "Register" button in the navbar opens the form, where I can put username and password to create a new account. The functionality worked as expected.

I also checked the link to the Login page at the bottom of the form, which worked well. 

##### Login
Clicking on the "Login" button in the navbar opens the form, allowing me to login to my existing account. I tried to leave empty fields or input incorrect details, but I was not able to submit the form if something was entered incorrectly. After a successful login I was redirected to the home page, seeing the message that I was logged in. 
I also checked the link to the Register page at the bottom of the form, which worked well.

##### Add New Recipe
I added plenty of test recipes to check  the functionality throughout the development.  If I leave some of the required fields empty, I will not be able to submit the form. I can see the flash messages displayed if my input does not meet length and/or complexity requirement. I also tried to create recipe without the URL image provided. Thankfully this is marked as requred and functions as expected. .

##### Edit Recipe
If I am the author of a recipe on the recipes page, I can see the buttons "Edit" and "Delete" on the single_recipe accordion tab. I searched and looked at someone else's recipes and the buttons were not displayed. I also tried to change the link manually in the browser to edit other's recipe. However, I was not able to open the form and got the message, that I can only edit my own recipes, which means defensive design works well against brute forcing.
Being the author of the recipe, I can view the form with pre-populated fields and can change anything that I want. If all fields are valid, I can see the changes I made on the "Recipes" Page after the submission. I tried to edit a number of recipes and edit different fields, everything worked correctly.

##### Delete Recipe
I deleted some dummy testing recipes to test the functionality. After clicking the "delete" button, the record is immediately deleted and this is flashed to the user for their convenience. 
Then I checked the database to make sure, that the recipe was removed. As well as that, I tested against brute-forcing, trying to delete another user's recipe(by changing the link manually in the browser), but wasn't able to do that.

##### Navbar
All links in the navbar were manually tested to ensure that they are pointing to the correct destination.   

##### Additional Information Relating to Manual Testing
Apart from that, I was manually testing the app with **debugger**: `debug=True` throughout all the development process. 
Every time when there was an error (when app crashed), the debugger displayed an error message to the view, that allowed me to find the location of the error and fix it.
I also have asked my friends, family members and fellow students in Slack to thoroughly test my website in different devices. So, a number of new accounts were created and new recipes added/edited and some of them were deleted. 
At that stage I got useful feedback and a few issues were found: 

##### Known bugs
 -  I accidentally broke my code, by changing all instances of cooking_method_name to cooking_method, which conflicted with other variables within the web app. Thankfully, using git.revert(), I was able to salvage my work and get back upto scratch. 

### Validators
#### Html
All the HTML files were tested through [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Since it does not recognize Jinja2 templating language, it showed a number of errors. Apart from that, no other errors were found across the html pages.

#### CSS
CSS files were tested through [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). This passed with no issues

#### JavaScript
JS file was tested through [Esprima](https://esprima.org/demo/validate.html) and [JSHint](https://jshint.com/) validators, code was syntactically valid.  "$" was not defined by JSHint (it is necessary for jQuery Materialize initializing).

#### Python
All python files were tested through [PEP8 Online](https://www.pythonchecker.com/) validator and were completely PEP8 compliant, 
except one thing:   
- in "_init_.py" file, the following import `from recipe-book import routes` has to be located at the bottom of the file
as it needs to import routes after the app has been initialised
to prevent circular imports.

### Compatibility and Responsiveness
This website was tested during it's development across **multiple browsers** (Chrome, Safary, Opera, FireFox, Internet Explorer) and on **multiple devices**: mobile (iPhone 5, 6, 8, Samsung Galaxy, Sony Xperia), tablets(iPad, iPadPro) and laptops (with HiDPI and MDPI and touch screens).     
As well as on **Google Chrome's developer tools** to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.   

---

## Deployment
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE  (I used [GitPod](https://www.gitpod.io/) online IDE for creating this project)
- [MongoDB Atlas](https://www.mongodb.com/) (for creation your database)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python](https://www.python.org/)   

#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/Jenkimdev/recipe_book` 

Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command into your terminal:   
`pip3 install -r requirements.txt`  
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*
5. Create a new Database called "recipe-book" in [MongoDB Atlas](https://www.mongodb.com/).   
*You can sign up for free account, if you do not have one.*
6. In "MyCookBook" database create five following collections:
###### cooking_methods
```
_id: <ObjectId>
cooking_method_name: <String>
```
###### diff_levels
```
_id: <ObjectId>
diff_level: <String>
```
###### users
```
_id: <ObjectId>
username: <String>
password: <String>
```
###### recipes
```
_id: <ObjectId>
recipe_name: <String>
prep_time: <String>
cook_time: <String>
completion_time: <String>
ingredients: <String>
method: <String>
diff_level: <String>
photo_path: <String>
cooking_method_name: <String>
recipe_author: <String>
image: <String>
```
7. You will now be able to run the application using the following command `python3 run.py`.   

### Heroku Deployment
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repository
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe, as I am in the UK, South Wales)
5. From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process, put the following command into the terminal: `heroku ps:scale web=1` to scale dynos
7. In the **Settings** tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:
    - **IP** : 0.0.0.0
    - **PORT** : 8080
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **DEBUG**: **FALSE**  
*Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file*

8. The app will be deployed and ready to run. Click "Open App" to view the app.   

**Note**: if you have not linked GitHub and Heroku following step N.5, alternatively as the last step of deployment, you can put the following command into your terminal:   
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.

---

## Credits for Content and Media
I used some of the logic from the non relational database management mini project to complete this project and many of the images within my databes, are borrowed from the BBC Goof Food website.
All recipes and recipes' images are taken from [BBC Good Food](https://www.bbcgoodfood.com/) except the ones added by other users.

### Code
1. [Stack Overflow](https://stackoverflow.com/), the Code Institute Slack were extremely helpful and useful during the process of building this project.
2. I constantly referred to the following documentation sources: [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [MongoDB](https://docs.mongodb.com/manual/).
3. The idea of using prefix-icons, asterixes and question-mark tooltips in forms was taken and modified from Tim Nelson's project.

### Acknowledgements
 I would like to thank everyone who has helped me throughout the development of this project.
 Code Institute tutors, fellow students, my friends and my family for the time, assistance and support!
 
---