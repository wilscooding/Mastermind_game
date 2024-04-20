from mastermind import check_guess

# Define test cases
test_cases = [
    ((0, 1, 3, 5), (2, 2, 4, 6), (0, 0)),  # "all incorrect"
    # "1 correct number and 1 correct location"
    ((0, 1, 3, 5), (0, 2, 4, 6), (1, 1)),
    # "1 correct number and 0 correct location"
    ((0, 1, 3, 5), (2, 2, 1, 1), (1, 0)),
    # "3 correct numbers and 2 correct location"
    ((0, 1, 3, 5), (0, 1, 5, 6), (3, 2))
]

# Run tests
for secret_code, guess, expected_feedback in test_cases:
    correct_numbers, correct_locations = check_guess(secret_code, guess)
    if correct_numbers == 0:
        feedback = "all incorrect"
    else:
        feedback = f"{correct_numbers} correct numbers and {correct_locations} correct location(s)"
    print(f"Secret Code: {secret_code}, Guess: {guess}")
    print(f"Feedback: {feedback}")
    print(f"Expected Feedback: {expected_feedback}")
    print("-" * 20)
