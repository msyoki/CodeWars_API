from app.models import Challenge
import unittest

class ChallengeTest(unittest.TestCase):
    '''
    Test class to test the behaviour of challenge class
    '''
    def setUp(self):
        '''
        setUp method to run before every test
        '''

        self.new_challenge=Challenge('5277c8a221e209d3f6000b56','valid-braces','algorithms','2013-11-05T00:07:31Z','javascript',"Write a function called `validBraces` that takes a string of braces, and determines if the order of the braces is valid. `validBraces` should return true if the string is valid, and false if it's invalid.\n\nThis Kata is similar to the Valid Parentheses Kata, but introduces four new characters. Open and closed brackets, and open and closed curly braces. Thanks to @arnedag for the idea!\n\nAll input strings will be nonempty, and will only consist of open parentheses '(' , closed parentheses ')', open brackets '[', closed brackets ']', open curly braces '{' and closed curly braces '}'. \n\n<b>What is considered Valid?</b>\nA string of braces is considered valid if all braces are matched with the correct brace. <br/>\nFor example:<br/>\n'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' would be considered invalid.\n\n\n<b>Examples:</b> <br/>\n`validBraces( \"(){}[]\" )` => returns true <br/>\n`validBraces( \"(}\" )` => returns false <br/>\n`validBraces( \"[(])\" )` => returns false <br/>\n`validBraces( \"([{}])\" )` => returns true <br/>\n")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_challenge,Challenge))


if __name__ == "__main__":
    unittest.main()