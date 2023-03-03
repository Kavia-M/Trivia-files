import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path ="postgres://{}:{}@{}/{}".format('student', 'student','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question = {
            "question": "In which year India got Independence?",
            "answer": "1947",
            "difficulty": 2,
            "category": 4
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["categories"]))
    
    def test_404_for_invalid_category_request(self):
        res = self.client().get("/categories/1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
    
    def test_get_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertLessEqual(len(data["questions"]), 10) #since questions per page is 10
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["categories"]))
        self.assertTrue(data["currentCategory"])
    
    def test_get_paginated_questions_with_valid_page_number(self):
        res = self.client().get("/questions?page=2")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertLessEqual(len(data["questions"]), 10) #since questions per page is 10
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["categories"]))
        self.assertTrue(data["currentCategory"])
    
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get("/questions?page=20")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
    
    def test_delete_question(self):
        res = self.client().delete('/questions/9')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 9).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 9)
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(question, None)
    
    def test_404_if_question_does_not_exist(self):
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
      
    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["totalQuestions"])

    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post("/questions/35", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")
    
    def test_get_question_search_with_results(self):
        res = self.client().post("/questions", json={"searchTerm": "who"}) 
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data['currentCategory'])

    def test_get_question_search_without_results(self):
        res = self.client().post("/questions", json={"searchTerm": "how many questions"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["totalQuestions"], 0)
        self.assertEqual(len(data["questions"]), 0)
        self.assertFalse(data['currentCategory'])
    
    def test_get_questions_by_category(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(len(data["questions"]))
        self.assertEqual(data['currentCategory'], 'Geography') #category ID 3 type is Geography
    
    def test_404_if_category_does_not_exist(self):
        res = self.client().get("/categories/10/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
    
    def test_get_question_not_in_previous_quesions_with_category(self):
        res = self.client().post('/quizzes', json={
            "previous_questions" : [16, 17],
            "quiz_category" : {
                "id" : 2,
                "type" : "Art"
            } 
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])
        question = data["question"]
        self.assertEqual(question["category"], 2)
        self.assertTrue(question["id"] not in [16, 17])
            
    def test_get_question_not_in_previous_quesions_without_category(self):
        res = self.client().post('/quizzes', json={
            "previous_questions" : [16, 17],
            "quiz_category" : {
                "id" : 0,
                "type" : None
            } 
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])
        question = data["question"]
        self.assertTrue(question["id"] not in [16, 17])

    def test_404_get_question_when_no_more_questions_remaining(self):
        res = self.client().post('/quizzes', json={
            "previous_questions" : [20, 21, 22],
            "quiz_category" : {
                "id" : 1,
                "type" : "Science"
            } 
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

        # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()