import unittest
from unittest.mock import patch
from io import StringIO
from mastermind import generate_secret_code, check_guess, play_mastermind


class TestMastermind(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=[[1], 'Enter number 2:', [2], 'Enter number 3:', [3], 'Enter number 4:', [4]])
    def test_play_mastermind(self, mock_input, mock_stdout):
        play_mastermind()
        output = mock_stdout.getvalue()
        expected_output = """
    Welcome to Mastermind! Try to guess the secret code using numbers from 0 to 7.
    You have 10 attempts to guess the correct number combinations. Good luck!

    Attempt # 1
    Enter number 1: Your guess: 1 2 3 4
    Feedback:

    Attempt # 2
    Enter number 2: Your guess: 1 2 3 4
    Feedback:

    Attempt # 3
    Enter number 3: Your guess: 1 2 3 4
    Feedback:

    Attempt # 4
    Enter number 4: Your guess: 1 2 3 4
    Feedback:

    Attempt # 5
    Enter number 5: Your guess: 1 2 3 4
    Feedback:
    """


    self.assertEqual(output, expected_output)


def test_check_guess(self):
    # Test Case 1: Exact Match of Guess with Secret Code
    secret_code = [1, 2, 3, 4]
    guess = [1, 2, 3, 4]
    self.assertEqual(check_guess(secret_code, guess), (4, 0))

    # Test Case 2: No Correct Numbers in Guess Positions
    secret_code = [1, 2, 3, 4]
    guess = [4, 3, 2, 1]
    self.assertEqual(check_guess(secret_code, guess), (0, 4))

    # Test Case 3: Mixture of Correct Positions and Incorrect Positions in Guess
    secret_code = [1, 2, 3, 4]
    guess = [1, 4, 2, 5]
    self.assertEqual(check_guess(secret_code, guess), (2, 1))

    # Test Case 4: No Correct Numbers in Guess
    secret_code = [1, 2, 3, 4]
    guess = [5, 6, 7, 0]
    self.assertEqual(check_guess(secret_code, guess), (0, 0))

    # Test Case 5: Handling Repeating Numbers in Secret Code and Guess
    secret_code = [1, 1, 2, 2]
    guess = [2, 2, 1, 1]
    self.assertEqual(check_guess(secret_code, guess), (0, 4))


if __name__ == '__main__':
    unittest.main()
