### Built With

Here are the frameworks used to bootstrap this project

* [![React][React.js]][React-url]
* [![Django][Django]][Django-url]

<!-- GETTING STARTED -->

## Getting Started

In order to run both servers of this project the following need to be installed:

* NodeJS
* Django
* djangorestframework
* requests
* django-cors-headers

### Installation

Each folder contains a project, one a django python api server, the other a react app for the UI.
To get the project running everything needs to be installed and configured for each folder

##### Backend

1. Ensure python packages listed above are installed
2. `cd backend`
3. `python manage.py makemigrations`
4. `python manage.py runserver`
5. Check that it's running as expected

#### Frontend

1. Ensure nodeJS is installed on your environment
2. `cd frontend`
3. `npm i` - installs all node packages needed

#### Launch with concurrently

1. Return to the root of the project, the pokeAPIfun folder
2. `npm i` - installs concurrently to launch both servers at once
3. `npm start` - launches both servers

