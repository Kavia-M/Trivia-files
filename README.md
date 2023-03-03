# The Game of Trivia - App
## API Development and Documentation

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game.

This project which aims in developting the api experience is the final project in the course `API Development and Documentation` which is a part of `Udacity nanodegree - Full Stack Development`.

The trivia app sees who's the most knowledgeable of the bunch. The application does the following:

1. Display questions - both all questions and by category. Questions shows the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app gives the ability to structure plan, implement, and test an API - skills essential for enabling future applications to communicate with others.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

## Getting started

### Backend
The backend directory contains the API and detailed API documentaion

#### Pre-requisites

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

##### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

#### Database Setup

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

#### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

#### Testing

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
cd backend
python test_flaskr.py
```

### Frontend

The frontend directory contains a complete React frontend to consume the data from the Flask server.

#### Pre-requisites

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend) so it will not load successfully if the backend is not working or not connected. I recommend that you **start up the backend first**, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

1. **Installing Node and NPM**
   This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**
   This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: `npm i`is shorthand for `npm install`

#### Running Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

#### Request Formatting

The frontend should be fairly straightforward and disgestible. While viewing the backend request handling and response formatting, you can reference the frontend to view how it parses the responses.

## API Reference

Please check [here](./backend/api-documentation.md) for detailed API documentation.

## Authors
- Kavia M from Natwest - an Udacity student

## Acknowledgements
Sincere Thanks to,
- Natwest Groups, for providing me an opportunity to take the nanodegree
- Coach Caryn, Udacity mentor for the API development and Documentation course
- Awanish Kumar Sigh, Natwest mentor for the nanodegree
- Udacity Team, for continous support and mentorship