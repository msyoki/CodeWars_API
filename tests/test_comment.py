import unittest
from app.models import Comment, Post

class CommentTest(unittest.TestCase):
    '''
    test class to test behaviour of comment class
    '''

    def setUp(self):
        '''
        setUp method to run before every test
        '''

        self.new_comment=Comment('very inspiring',1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))



class PostTest(unittest.TestCase):
    '''
    test class to test the behaviour of post class
    '''
    def setUp(self):
        '''
        setUp method to run before every test
        '''

        self.new_post=Post('Addition','Add two arrays together','Business','013-11-05T00:07:31Z',1,0,3)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))



if __name__ == "__main__":
    unittest.main()