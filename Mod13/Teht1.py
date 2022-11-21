# Toteuta Flask-taustapalvelu, joka ilmoittaa,
# onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/alkuluku/<number>')
def summa(number):
    try:
        number = int(number)
        statuscode = 200

        def num_chk(number):
            if number > 1:
                for n in range(2, number):
                    if (number % n) == 0:
                        return False
                return True
            else:
                return False

        response = {
            "number": number,
            "isPrime": num_chk(number)

        }

    except ValueError:
        statuscode = 400
        response = {
            "status": statuscode,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=statuscode, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(statuscode):
    response = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonresp = json.dumps(response)
    return Response(response=jsonresp, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
