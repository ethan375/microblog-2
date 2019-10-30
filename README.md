This app in its current form is a web server built on the flask framework in python.

the app utilizes python 3.7, pipenv, flask, and flake 8

To run the app:

1. clone it to your machine
2. enter into a virtual env or pip env
3. install the dependencies found in the Pipfile
4. once everything has finished installing run `flask run`
once the dev server is up navigate to localhost:5000 in your web browser

navigating to `localhost:5000/` or `localhost:500/index` will render an html template and display posts from users 

There is now a login page with a link at the top of the home page, the login form is sort of a 'dummy' because it is not currently hooked into a database.

In this release there are no new routes to check out. There has been a database setup using sqlite. Added users and posts classes/columns