import random

# Function to provide hints based on previous guesses and feedback


def provide_hint(secret_code, previous_guesses, previous_feedback):
    """Provide hints based on the player's previous guesses and feedback.

    Args:
        secret_code (list[int]): The secret code.
        previous_guesses (list[list[int]]): The list of previous guesses.
        previous_feedback (list[tuple[int, int]]): The list of previous feedback.

    Returns:
        list[str]: A list of hints.
    """
    incorrect_positions = set()  # Set to store incorrect positions
    # Set to store correct numbers in wrong positions
    wrong_numbers = set()

    # Analyze previous feedback to identify numbers in wrong positions
    for guess, feedback in zip(previous_guesses, previous_feedback):
        if feedback != (4, 4):  # If the guess is not correct
            for i, num in enumerate(guess):
                # If the number is in the secret code but not in the correct position
                if num in secret_code and num != secret_code[i]:
                    incorrect_positions.add(i)
                # If the number is correct but in the wrong position
                elif num not in secret_code:
                    wrong_numbers.add(num)

    hints = []  # List to store hints

    # Generate hints based on incorrect positions
    for position in incorrect_positions:
        hints.append(
            f"Number at position {position + 1} is in wrong position.")

    # Generate hints based on wrong numbers
    for num in wrong_numbers:
        if num >= max(wrong_numbers):
            hints.append(f"Number {num} should be lower.")
        else:
            hints.append(f"Number {num} should be higher.")

    # Randomly choose between incorrect positions and wrong numbers for the hint
    if hints:
        hint = random.choice(hints)
        return [hint]
    else:
        return []
