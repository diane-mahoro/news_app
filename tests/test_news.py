import unittest
from .models import Sources
Sources=models.Sources

class NewsTest(unittest.TestCase):
    '''
    Test class to test  the behaviour of the News class
    '''
    def setUp(self):
        self.new_article=Sources(1,"brabra","dfhsjn","fddsec","descdscx")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Sources))

if __name__ == '__main__':
    unittest.main()
     
