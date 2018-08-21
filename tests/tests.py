import unittest
import requests

class BaseCase(unittest.TestCase):
    
    def setup(self,all_questions_list,answers):
        self.all_questions=all_questions_list
        self.all_answers=answers
    def test_all_questions(self):
        response=requests.get('http://localhost:5000/api/v1/questions')
        self.assertEqual(response,[200])
        
        
  