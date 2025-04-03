import unittest
from src.chatbot import ChatBot

class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatBot()

    def test_chat_response(self):
        # Test a simple question
        response = self.chatbot.chat("Hello, how are you?")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_error_handling(self):
        # Test error handling with invalid input
        response = self.chatbot.chat("")
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main() 