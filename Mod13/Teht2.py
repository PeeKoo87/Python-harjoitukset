import mysql.connector
from flask import Flask, Response
import json

link = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Sal41a6sana52S',
    autocommit=True
)

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def go_fetch_it(icao):
    try:

        icao = str.upper(icao)
        status_code = 200
        cursor = link.cursor()
        cursor.execute("select name, municipality from airport where ident ='" + icao + "'")
        find = cursor.fetchone()

        if find != None:
            airport = find[0]
            municipality = find[1]
            response = {
                "ICAO": icao,
                "Airport": airport,
                "Municipality": municipality
            }

    except ValueError:
        status_code = 400
        response = {
            "status": status_code,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=status_code, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(status_code):
    response = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)