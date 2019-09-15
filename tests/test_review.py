import unittest
from .models import Articles
Articles=models.Articles

class NewsTest(unittest.TestCase):
    '''
    Test class to test  the behaviour of the Articles class
    '''
    def setUp(self):
        self.new_article=Articles("hello","brabra","dfhsjn","fddsec","descdscx","sdfgvh","hfghbjn")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
    unittest.main()
    