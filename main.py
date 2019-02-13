import requests
import sys
from time import sleep

# Ricezione della risposta dall' API endpoint nomi astronauti.

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# Ricezione della risposta dall' Api endopoint posizione ISS

response = requests.get("http://api.open-notify.org/iss-now.json")
posizione = response.json()

# Funzione per effetto digitazione


def delay(testo):
    for x in testo:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    print("")


# Funzione per effetto transizione


def transizione():
    print(" ")
    delay("...")
    delay("...")
    delay("...")
    print(" ")


# Messaggio di benvenuto e presentazione funzionalità

delay('''Benvenuti.
Questo programma vi permetterà di consocere:
1) Quanti astronuati sono nello spazio in questo momento
2) I loro nomi
3) # Dove si trova la Stazione Spaziale Internazionale
4) # L'esatto momento in cui orbiterà sopra di voi''')

transizione()

# Conferma per procedere

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

# NUMERO DI PERSONE NELLO SPAZIO

while True:
    transizione()
    numero = input("Vuoi sapere quante persone sono nello spazio in questo momento?(S/N): ").strip().lower()

    if numero == "s":
        number = (data["number"])
        print("Attualmente ci sono", number, "persone nello spazio.")
        break
    elif numero == "n":
        uscita_1 = input("Desideri uscire dal programma?(S/N): ").strip().lower()
        if uscita_1 == "s":
            exit()
        elif uscita_1 == "n":
            break
    else:
        print("Per favore, inserire una risposta valida.")


# NOMI ASTRONAUTI

while True:
    transizione()
    nomi = input("Vuoi conoscere i nomi degli astronauti attualmente nello spazio?(S/N): ").strip().lower()

    if nomi == "s":
        for i in range(len(data)):
            nome = (data["people"][i]["name"])
            string = "Nome: {}"
            output = string.format(nome)
            delay(output)
        break
    elif nomi == "n":
        uscita_2 = input("Desideri uscire dal programma?(S/N): ").strip().lower()
        if uscita_2 == "s":
            exit()
        elif uscita_2 == "n":
            break
    else:
        print("Per favore, inserire una risposta valida.")

# POSIZIONE ISS

while True:
    transizione()
    posizione_now = input("Vuoi conoscere la posizione attuale dell' ISS?(S/N): ").strip().lower()

    if posizione_now == "s":
        latitudine = (posizione["iss_position"]["latitude"])
        longitudine = (posizione["iss_position"]["longitude"])
        timestamp = (posizione["timestamp"])
        print("Latitudine: ", latitudine)
        print("Longitudine: ", longitudine)
        print("Timestamp: ", timestamp)
        break
    elif posizione_now == "n":
        uscita_3 = input("Desideri uscire dal programma?(S/N): ").strip().lower()
        if uscita_3 == "s":
            exit()
        elif uscita_3 == "n":
            break
    else:
        print("Per favore, inserire una risposta valida.")
