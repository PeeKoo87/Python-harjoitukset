#Toteuta Flask-taustapalvelu, joka ilmoittaa,
# onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
IntChk = int(input("anna kokonaisluku: "))
for i in range(2, IntChk):
    if IntChk % i == 0:
        print("luku ei ole alkuluku")
        break

else:
    print("luku on alkuluku")

from flask import Flask, request

app = Flask(__name__)
@app.route('/PrimeNumber')

def isPrime(luku):
    args = request.args
    luku = float(args.get("luku"))
    for i in range(2, luku):
        if IntChk % i == 0:

            isPrime = {
                luku : int(luku),

            }

            return isPrime

    number = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1+luku2

    result1 = {
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa
    }

    return vastaus




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)