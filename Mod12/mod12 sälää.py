import requests

query_parameter = input("Anna hakusana ")
url = f"https://api.tvmaze.com/search/shows?q={query_parameter}"
try:
    response = requests.get(url)
    """""
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0: #jos for looppia käytetään niin tätä ei tarvitse.
            print(f"1.hakutuloksen nimi: {data[0]['show']['name']}")
            print(f"pojot: {round(data[0]['score']*10)}")
    
        else:
            print("ei hakutuloksia")
    """""
    if response.status_code == 200:
        data = response.json()
        if len(data) == 0: #jos for looppia käytetään niin tätä ei tarvitse.
            print("ei hakutuloksia")
        for item in data:
            print(f"1.hakutuloksen nimi: {item['show']['name']}")
            print(f"pojot: {round(item['score']*10)} "
                  f"lisätietoa: {item['show']['url']}")


    else:
        print(f"Viallinen osoite, error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("jotain meni pieleen: " + str(e))