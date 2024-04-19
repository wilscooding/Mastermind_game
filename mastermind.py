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


print(generate_secret_code())
