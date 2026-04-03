""" Run tests of the emotion_dector app """
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """ All tests appear below and should result in an OK """

    def test_joy(self):
        """ Test for joy """
        result = emotion_detector("I am glad this happened")
        self.assertIn("joy", str(result).lower())

    def test_anger(self):
        """ Test for anger """
        result = emotion_detector("I am really mad about this")
        self.assertIn("anger", str(result).lower())

    def test_disgust(self):
        """ Test for ddisgust is """
        result = emotion_detector("i feel disgusted just hearing about this")
        self.assertIn("disgust", str(result).lower())

    def test_sadness(self):
        """ Test for sadness """
        result = emotion_detector("I  am so sad about this")
        self.assertIn("sadness", str(result).lower())

    def test_fear(self):
        """ Test for fear """
        result = emotion_detector(" am really afraid that this will happen")
        self.assertIn("fear", str(result).lower())

if __name__ == "__main__":
    unittest.main()
