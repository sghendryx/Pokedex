### Built With

Here are the frameworks used to bootstrap this project

* [![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/docs/getting-started.html)
* [![Material-UI](https://img.shields.io/badge/Material--UI-0081CB?style=for-the-badge&logo=material-ui&logoColor=white)](https://mui.com/material-ui/react-button/)
* [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.1/intro/overview/)

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

