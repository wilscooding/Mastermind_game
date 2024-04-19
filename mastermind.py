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


print(generate_secret_code())
