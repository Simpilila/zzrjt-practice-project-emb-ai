"""Unit tests for the EmotionDetection package."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_emotion_for_joy(self):
        """Test that 'I am glad this happened' has joy as dominant emotion."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_for_anger(self):
        """Test that 'I am really mad about this' has anger as dominant emotion."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_for_disgust(self):
        """Test that 'I feel disgusted just hearing about this' has disgust as dominant."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_for_sadness(self):
        """Test that 'I am so sad about this' has sadness as dominant emotion."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_for_fear(self):
        """Test that 'I am really scared about this' has fear as dominant emotion."""
        result = emotion_detector('I am really scared about this')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
