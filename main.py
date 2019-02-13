import requests
import sys
from time import sleep

# Ricezione della risposta dall' API endpoint.

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# Funzione per effetto digitazione


def delay(testo):
    for x in testo:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    print("")


# Messaggio di benvenuto e presentazione funzionalità

delay('''Benvenuti.
Questo programma vi permetterà di consocere:
1) Quanti astronuati sono nello spazio in questo momento
2) I loro nomi
3) # Dove si trova la Stazione Spaziale Internazionale
4) # L'esatto momento in cui orbiterà sopra di voi''')

# Loop e if per gestire le possibili combinazioni

while True:
    continua = input("Vogliamo procedere?(S/N): ").strip().lower()
    if continua == "s":
        break
    elif continua == "n":
        uscita = input("Desideri uscire dal programma?(S/N): ").strip().lower()
        if uscita == "s":
            exit()
        elif uscita == "n":
            break
    else:
        print("Per favore, inserire una risposta valida.")

while True:
    numero = input("Vuoi sapere quante persone sono nello spazio in questo momento?(S/N): ").strip().lower()

    if numero == "s":
        number = (data["number"])
        print(number)
        break
    elif numero == "n":
        break

nomi = input("Vuoi conoscere i nomi degli astronauti attualmente nello spazio?(S/N): ").strip().lower()

if nomi == "s":
    for i in range(len(data)):
        nome = (data["people"][i]["name"])
        string = "Nome: {}"
        output = string.format(nome)
        print(output)
elif nomi == "n":
    pass
