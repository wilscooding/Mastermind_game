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
            if len(set(numbers)) == len(numbers):
                return numbers  # Unique numbers found
        else:
            print("Error generating secret code.")
            return None


def check_guess(secret_code, guess):
    correct_numbers_and_positions = 0
    correct_numbers_only = 0

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_numbers_and_positions += 1
        elif guess[i] in secret_code:
            correct_numbers_only += 1

    return correct_numbers_and_positions, correct_numbers_only


secret_code = generate_secret_code()
print("Secret Code: ", secret_code)

guess = [1, 3, 4, 6]
result = check_guess(secret_code, guess)
print("Result:", result)
