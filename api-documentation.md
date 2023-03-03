# API Documentation
The Trivia app is a quiz app. The API is for listing out the questions based on category if requested, search for questions, delete a question, to create a new question in the app and to retieve the questions when playing the game. There are two tables in the `trivia` database namely `question` and `category`.

## Getting started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 

## Errors
Errors are returned as JSON objects in the following format:
```json
{
    "success" : false,
    "error": 404,
    "message": "resource not found"
}
```
The possible errors are:

Error code | Error type |
--- | --- |
400 | Bad request
404 | Resource Not Found
405 | Method not allowed
422 | Unprocessable
500 | Internal Server Error

## Endpoints

### `GET '/categories'`
- General:
    - Returns success and the list of categories from the `category` table as a json with `id` as key and `type` as value
    - In Frontend, this is used to display the categories to choose in question list page and while playing the game
- **Possible errors** : 
    - ***404*** if no category exists in the database
- Sample: `curl http://127.0.0.1:5000/categories`

```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```

### `GET '/questions?page=${integer}'`
- General:
    - Fetches a paginated set of questions, a total number of questions, all categories and current category string
    - Request Arguments: `page` - integer which is optional and is default `1`
    - Returns: An object with 10 paginated questions, total questions which is overall total number of questions in the database, object including all categories, current category string and also success boolean value
- **Possible errors** : 
    - ***404*** for invalid page number
- Sample: `curl http://127.0.0.1:5000/questions?page=2`

```json
{
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist-initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "totalQuestions": 19,
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "currentCategory": "Geography", 
  "success": true
}
```

### `GET '/categories/${id}/questions'`
- General:
    - Fetches questions for a cateogry specified by id request argument
    - Request Arguments: `id` - integer which is category id
    - Returns: An object with questions for the specified category in the page, total number of questions of the category, current category string and success boolean
- **Possible errors** : 
    - ***404*** if no questions found with the given category id
- Sample: `curl http://127.0.0.1:5000/categories/3/questions`

```json
{
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "totalQuestions": 3,
  "currentCategory": "Geography", 
  "success": true, 
}
```

### `DELETE '/questions/${id}'`
- General:
    - Deletes a specified question using the id of the question
    - Request Arguments: `id` - integer which is question id
    - Returns the success boolean value, id of the deleted question,  the questions in the page after deletion and total number of questions after deletion
- **Possible errors** : 
    - ***404*** if the given question id does not exists
    - ***422*** if some error during deletion from the database
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/5`

```json
{
  "deleted": 5, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "totalQuestions": 18,
  "success": true
}
```

### `POST '/questions'`
- General:
    - Sends a post request in order to add a new question
    - Request Body:
    ```json
    {
      "question": "In which year India got Independence?",
      "answer": "1947",
      "difficulty": 2,
      "category": 4
    }
    ```
    - It inserts the new question to the database and returns success boolean value, id of the question that is created, questions in the page after insertion and total number of questions after insertion
- **Possible errors** : 
    - ***422*** if some error occurs during insertion into the database
- Sample: `curl -H 'Content-Type: application/json' -d '{ "question":"In which year India got Independence?","answer":"1947", "difficulty": 2, "category" : 4}' -X POST http://127.0.0.1:5000/questions`

```json
{
  "created": 24, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "totalQuestions": 19,
  "success": true
}
```

### `POST '/questions'`
- General:
    - Sends a post request in order to search for a specific question by search term
    - Request Body:
    ```json
    {
      "searchTerm": "who"
    }
    ```
    - Searches for the questions where search term is a substring of the question string case insensitive
    - Returns: array of questions that matches the search term with pagination, a number of totalQuestions that met the search term, the current category string and also success boolean value
    - Returns an empty array and totalQuestions as 0 if no question matches the search parameter
- **Possible errors** : 
    - ***422*** unprocessable error 
- Sample: `curl -H 'Content-Type: application/json' -d '{"searchTerm":"who"}' -X POST http://127.0.0.1:5000/questions`
    
```json
{
  "questions": [
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "totalQuestions": 2,
  "currentCategory": "History", 
  "success": true
}
```

### `POST '/quizzes'`
- General:
    - Sends a post request in order to get the next question with request body that has category id and ids of previous questions as parameters
    - Returns success boolean value and a random question that is not one of the previous questions and is within the given category is category is given
- **Possible errors** : 
    - ***404*** if there is no more questions in the given category
- Sample:`curl -H 'Content-Type: application/json' -d '{ "previous_questions": [16, 17], "quiz_category" : {"id" : 2, "type" : "Art" }  }' -X POST http://127.0.0.1:5000/quizzes`

```json
{
  "question": {
    "answer": "Jackson Pollock", 
    "category": 2, 
    "difficulty": 2, 
    "id": 19, 
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
  }, 
  "success": true
}
```
    
    