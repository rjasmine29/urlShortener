# URL Shortener

This project is on a URL shortener.

## Installation & Usage

* Run `pipenv install` to install dependencies
* `pipenv shell`
* cd into pairedWork folder
* cd into project folder
* Run `python manage.py` runserver
* Type in a url, and retrieve a shortened url
* Copy and paste the shortened url onto a browser 

### Requirements

All requirements were met:

* Users should be able to enter a url into an input box on your website's front page
* Your backend will then generate a shortened path at which a User can access their url
* You must implement Python in some capacity in this application
* Store this shortened path and it's longer counterpart in a database
* No login should be required to create a shortened URL
* If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to
* If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL

### Bugs
* Users will have to manually copy and paste the shortened url instead of being able to click on it and directly taking them to the url. 

### Wins and Challenges
#### Wins:
* All requirements were met
* The user is able to get a shortened url

Challenges:
* There were problems with getting the shortened url to work
* There is currently no styling, this will need to be added 
