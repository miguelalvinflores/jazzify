# Jazzify
![GitHub last commit](https://img.shields.io/github/last-commit/miguelalvinflores/jazzify)
![GitHub pull requests](https://img.shields.io/github/issues-pr/miguelalvinflores/jazzify)

<!-- Insert Usage GIF here -->
![Site Demo Gif](JazzifyGIF3Mb.gif)

## Brief Introduction

Jazzify is a website for jazzheads to listen to a privately selected library of all time jazz greats.

All music is sourced from publicly available libraries and collections under: 

<a href="https://archive.org/" target="_top">Internet Archive Website</a>

# Table of contents


- [Jazzify](#Jazzify)
- [Brief Description](#brief-introduction)
- [Table of contents](#table-of-contents)
- [Live Link](#live-link)
- [Technologies](#technologies)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Hosting](#hosting)
- [Features](#features)


## [Live Link](**https://jazzify-aa.herokuapp.com/**)

<a href="https://jazzify-aa.herokuapp.com/" target="_top">Jazzify Website</a>

<!-- Insert Usage GIF here -->

## Technologies

Jazzify is built using the following stack & libraries:

### **Backend**
1. _Sequelize_
   * Sequelize is a promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server. It features solid transaction support, relations, eager and lazy loading, read replication and more.
2. _PostgreSQL_
   * PostgreSQL is a relational database management system emphasizing extensibility and SQL compliance.
3. _Python_
   * web applications can send and retrieve data from a server asynchronously without interfering with the display and behaviour of the existing page.
4. Internet Archive API
   * The Internet Archive is an American digital library with the stated mission of "universal access to all knowledge". It provides free public access to collections of digitized materials, including websites, software applications/games, music, movies/videos, moving images, and millions of books. This is the source of the media files.

### **Frontend**

1. _Javascript_
2. _React.js_
   * React is a declarative, efficient, and flexible JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called “components”.

### **Hosting**
1. Heroku
   * Heroku is a platform as a service that enables developers to build, run, and operate applications entirely in the cloud.

## Features

Please take a look at our Wiki for a full list of features, and upcoming features

<a href="https://github.com/miguelalvinflores/jazzify/wiki" target="_top">Jazzify Wiki</a>


<!-- # Footer -->
[(Back to top)](#table-of-contents)

Leave a star in GitHub and share this guide if you found this helpful.







<!-- Add the footer (.png) here -->


## Getting started (if forking or cloning)

1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/appacademy-starters/python-project-starter.git
   ```

2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.



## Deploy to Heroku

***
*IMPORTANT!*
   If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment.
   You can do this by running:

   ```bash
   pipenv lock -r > requirements.txt
   ```

*ALSO IMPORTANT!*
   psycopg2-binary MUST remain a dev dependency because you can't install it on apline-linux.
   There is a layer in the Dockerfile that will install psycopg2 (not binary) for us.
***

1. Create a new project on Heroku
2. Under Resources click "Find more add-ons" and add the add on called "Heroku Postgres"
3. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
4. Run

   ```bash
   heroku login
   ```

5. Login to the heroku container registry

   ```bash
   heroku container:login
   ```

6. Update the `REACT_APP_BASE_URL` variable in the Dockerfile.
   This should be the full URL of your Heroku app: i.e. "https://flask-react-aa.herokuapp.com"
7. Push your docker container to heroku from the root directory of your project.
   This will build the dockerfile and push the image to your heroku container registry

   ```bash
   heroku container:push web -a jazzify-aa
   ```
   OR
   ```bash
   heroku container:push web -a jazzify-aa -
   ```

8. Release your docker container to heroku

   ```bash
   heroku container:release web -a jazzify-aa
   ```

9. set up your database:

   ```bash
   heroku run -a jazzify-aa flask db upgrade
   heroku run -a jazzify-aa flask seed all
   ```

10. Under Settings find "Config Vars" and add any additional/secret .env variables.


[(Back to top)](#table-of-contents)

Leave a star in GitHub and share this guide if you found this helpful.

