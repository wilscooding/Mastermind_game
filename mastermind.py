import requests


# Function to generate the secret code using RANDOM.ORG API
def generate_secret_code():
    url = "https://www.random.org/integers/"
    params = {
        "num": 4,  # Generate 4 numbers
        "min": 0,
        "max": 7,
        "col": 1,
        "base": 10,
        "format": "plain",
        "rnd": "new"
    }

    # Generate numbers until they are unique
    while True:
        response = requests.get(url, params=params)
        print(response.text)
        if response.status_code == 200:
            numbers = [int(num) for num in response.text.strip().split("\n")]
            # if len(set(numbers)) == len(numbers):
            return numbers  # Unique numbers found
        else:
            print("Error generating secret code.")
            return None


def check_guess(secret_code, guess):
    correct_numbers_and_positions = 0
    correct_numbers_only = 0
    used_indices = set()

    # Count correct numbers and positions
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_numbers_and_positions += 1
            used_indices.add(i)

    # Count correct numbers only
    for i in range(len(secret_code)):
        if guess[i] != secret_code[i] and guess[i] in secret_code and secret_code.index(guess[i]) not in used_indices:
            correct_numbers_only += 1
            used_indices.add(secret_code.index(guess[i]))

    return correct_numbers_and_positions, correct_numbers_only


def play_mastermind():
    secret_code = generate_secret_code()
    attempts = 0
    print("secret code", secret_code)

    print("Welcome to Mastermind! Try to guess the secret code using numbers from 0 to 7.")
    print("You have 10 attempts to guess the correct number combinations. Good luck!")

    while attempts < 10:
        print(f"\nAttempt # {attempts + 1}")

        guess = []
        for i in range(4):
            guess.append(int(input(f"Enter number {i+1}: ")))

        correct_number_and_positions, correct_numbers_only = check_guess(
            secret_code, guess)

        if correct_number_and_positions == 4:
            print("Congratulations! You've guessed the secret code")
            break

        print("Your guess:", ' '.join(map(str, guess)))

        feedback = ""
        if correct_number_and_positions == 0 and correct_numbers_only == 0:
            feedback = "all incorrect"
        else:
            if correct_number_and_positions > 0:
                feedback += f"{correct_number_and_positions} correct number(s) and position(s)"
            if correct_numbers_only > 0:
                if feedback:
                    feedback += ", and "
                feedback += f"{correct_numbers_only} correct number(s) only"

        print("Feedback:", feedback)
        attempts += 1

    if attempts == 10:
        print("\nSorry, you're out of attempts. The secret code was: ", secret_code)


play_mastermind()
