import requests
import json
url = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        response_json = json.loads(response.content)
        joke = response_json.get('value')

        print(joke)


    else:
        print(f"Viallinen osoite, error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("jotain meni pieleen: " + str(e))