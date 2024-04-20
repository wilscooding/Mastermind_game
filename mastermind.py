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
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [int(num) for num in response.text.strip().split("\n")]
    else:
        print("Error generating secret code.")
        return None

# Function to check the player's guess against the secret code


# def check_guess(secret_code, guess):
#     correct_numbers = sum(1 for i in guess if i in secret_code)
#     correct_locations = sum(1 for i, j in zip(secret_code, guess) if i == j)
#     return correct_numbers, correct_locations

def check_guess(secret_code, guess):
    correct_numbers = 0
    correct_locations = 0

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_numbers += 1
            correct_locations += 1
        elif guess[i] in secret_code:
            correct_numbers += 1

    return correct_numbers, correct_locations


def play_mastermind():
    secret_code = generate_secret_code()
    attempts = 0
    print(secret_code)

    print("Welcome to Mastermind! Try to guess the secret code using numbers from 0 to 7.")
    print("You have 10 attempts to guess the correct number combinations.")

    while attempts < 10:
        print(f"\nAttempt #{attempts + 1}")

        # Get player's guess
        guess = []
        for i in range(4):
            guess.append(int(input(f"Enter number {i + 1}: ")))

        if all(num not in secret_code for num in guess):
            print("Feedback: all incorrect")
            attempts += 1
            continue

        # Check the guess
        correct_numbers, correct_locations = check_guess(secret_code, guess)

        if correct_locations == 4:
            print("Congratulations! You've guessed the secret code!")
            break

        # Provide feedback
        print(
            "Feedback:", f"{correct_numbers} correct numbers and {correct_locations} correct location(s).")

        attempts += 1
        print(f"Attempts remaining: {10 - attempts}")

    if attempts == 10:
        print("Sorry, you've run out of attempts. The secret code was:", secret_code)


if __name__ == "__main__":
    # Start the game
    play_mastermind()
