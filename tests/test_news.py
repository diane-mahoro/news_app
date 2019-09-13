import unittest
from .news import News
News=news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test  the behaviour of the News class
    '''
    def setUp(self):
        self.new_article=News(1,"brabra","dfhsjn","fddsec","descdscx")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,News))

if __name__ == '__main__':
    unittest.main()
     
