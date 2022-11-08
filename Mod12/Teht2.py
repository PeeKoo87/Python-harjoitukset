import requests
import json



try:
    region = input("Miltä paikkakunnalta haluat tiedot?")

    url1 = f"https://api.openweathermap.org/data/2.5/weather?q={region}&appid=4495b175fb1e94fe275cdaab54689296"

    response = requests.get(url1)

    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            print("ei hakutuloksia")

        response_json = json.loads(response.content)
        weather = response_json.get('weather')

        for w in weather:
            a = f"In {region} current weather type is: {w['main']}/{w['description']}"

        #main = response_json.get('main')
        #for m in main:
            #b = (f"{m['temp']}")

       # #en saanut lämpötiloja toimimaan jostain syystä.# #

        print(a)

    else:
        print(f"Viallinen osoite, error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("jotain meni pieleen: " + str(e))