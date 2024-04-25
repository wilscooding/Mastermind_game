import requests
from extensions.hints_extension import provide_hint


def generate_secret_code():
    """Generate a secret code using the RANDOM.ORG API.

        Returns:
            list[int]: The generated secret code.
    """
    url = "https://www.random.org/integers/"
    params = {
        "num": 4,
        "min": 0,
        "max": 7,
        "col": 1,
        "base": 10,
        "format": "plain",
        "rnd": "new"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [int(num) for num in response.text.strip().split("\n")]
    else:
        print("Error generating secret code.")
        return None


# Function to check the player's guess against the secret code
def get_valid_guess(guess_number):
    """Prompt the player to enter a valid guess.

    Args:
        guess_number (int): The number of the current guess.

    Returns:
        int: The player's valid guess.
    """
    while True:
        guess = input(f"Enter a number {guess_number}: ")
        try:
            guess = int(guess)
            if 0 <= guess <= 7:
                return guess
            else:
                raise ValueError("Number out of range")
        except ValueError as e:
            print(
                f"Invalid input: {e}. Please enter a valid number from 0 to 7.")


def check_guess(secret_code, guess):
    """Check the player's guess against the secret code.

    Args:
        secret_code (list[int]): The secret code.
        guess (list[int]): The player's guess.

    Returns:
        tuple[int, int]: The number of correct numbers and their correct locations.
    """
    correct_numbers = 0
    correct_locations = 0
    secret_code_counts = {}  # Track the counts of numbers in the secret code
    guess_counts = {}  # Track the counts of numbers in the guess

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_locations += 1
        secret_code_counts[secret_code[i]] = secret_code_counts.get(
            secret_code[i], 0) + 1
        guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1

    for num in guess_counts:
        if num in secret_code_counts:
            correct_numbers += min(secret_code_counts[num], guess_counts[num])

    return correct_numbers, correct_locations


def print_previous_guesses_and_feedback(previous_guesses, previous_feedback):
    """Print the player's previous guesses and their corresponding feedback.

    Args:
        previous_guesses (list[list[int]]): The list of previous guesses.
        previous_feedback (list[str | tuple[int, int]]): The list of previous feedback.
    """
    for guess, feedback in zip(previous_guesses, previous_feedback):
        if feedback != "all incorrect":
            print(f"guess: {guess}, Feedback: {feedback}")
        else:
            print(f"guess: {guess} Feedback: all incorrect")


def play_mastermind():
    """Play the Mastermind game."""
    while True:  # Main game loop
        secret_code = generate_secret_code()
        attempts = 0
        print(secret_code)

        print("**************************Welcome to Mastermind!**************************")
        print("In this game, you need to guess the secret code using numbers from 0 to 7.")
        print("The secret code consists of a combination of 4 numbers.")
        print("You can request hints after your first attempt.")
        print(
            "Additionally, you can request to view previous feedback after the 2nd attempt.")

        while attempts < 10:
            print(f"\nAttempt #{attempts + 1}")

            guess = []
            for i in range(4):
                valid_guess = get_valid_guess(i + 1)
                guess.append(valid_guess)

            # Display the guesses
            print("\nYour guess:", " ".join(map(str, guess)))

            if attempts >= 0:
                # Ask if the player wants a hint after the first attempt
                hint_request = input("Would you like a hint? (yes/no)\n")
                if hint_request.lower() == "yes":
                    hint = provide_hint(
                        secret_code, [guess], [(0, 0)])
                    print(f"Hint: {hint}\n")

                if attempts >= 1:
                    view_previous = input(
                        " Would you like to view previous guesses and their feedback? (yes/no)\n")
                    if view_previous.lower() == "yes":
                        print_previous_guesses_and_feedback(
                            previous_guesses, previous_feedback)

            if all(num not in secret_code for num in guess):
                print("Feedback: all incorrect")
                attempts += 1
                previous_guesses.append(guess)
                previous_feedback.append("all incorrect")
                continue

            # Check the guess
            correct_numbers, correct_locations = check_guess(
                secret_code, guess)

            if correct_locations == 4:
                print("Congratulations! You've guessed the secret code!")
                break

            # Provide feedback
            print(
                "Feedback:", f"{correct_numbers} correct numbers and {correct_locations} correct location(s).")

            attempts += 1
            print(f"Attempts remaining: {10 - attempts}")

            previous_guesses.append(guess)
            previous_feedback.append((correct_numbers, correct_locations))

        if attempts == 10:
            print("Sorry, you've run out of attempts. The secret code was:", secret_code)

        play_again = input("Would you like to play again? (yes/no)\n").lower()
        if play_again != 'yes':
            break  # Exit the main game loop if the player chooses not to play again


previous_guesses = []
previous_feedback = []


if __name__ == "__main__":
    # Start the game
    play_mastermind()
