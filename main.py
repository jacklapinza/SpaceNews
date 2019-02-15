import requests
import sys
from time import sleep
import webbrowser
import datetime


# Ricezione della risposta dall' API endpoint nomi astronauti.

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# Ricezione della risposta dall' Api endopoint posizione ISS

response = requests.get("http://api.open-notify.org/iss-now.json")
posizione = response.json()


# Funzione per effetto digitazione


def delay(testo):
    for x in testo:
        print(x, end="")
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


# Funzione per effetto micro_transizione


def microtras():
    print("")


# Funzione per effetto display informazione

def effetto(testo):
    print("")
    for x in testo:
        print("#", end="")
    print("")
    print(testo)

    for x in testo:
        print("#", end="")
    print("")


# Messaggio di benvenuto e presentazione funzionalità

microtras()
delay("Benvenuti!")
microtras()
delay("Questo programma vi permetterà di consocere: ")
microtras()
delay('''1) Quanti astronuati sono nello spazio in questo momento
2) I loro nomi
3) Dove si trova la Stazione Spaziale Internazionale
4) L'esatto momento in cui orbiterà sopra di voi''')

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

# NUMERO DI PERSONE NELLO SPAZIO. ps -> persone spazio

while True:
    transizione()
    numero = input("Vuoi sapere quante persone sono nello spazio in questo momento?(S/N): ").strip().lower()

    if numero == "s":
        number = (data["number"])
        numero_pers = "Attualmente ci sono {} persone nello spazio."
        numero_persone = numero_pers.format(number)
        effetto(numero_persone)
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
    microtras()
    nomi = input("Vuoi conoscere i nomi degli astronauti attualmente nello spazio?(S/N): ").strip().lower()

    if nomi == "s":
        for i in range(len(data)):
            nome = (data["people"][i]["name"])
            string = "Nome: {}"
            output = string.format(nome)
            effetto(output)
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
    microtras()
    posizione_now = input("Vuoi conoscere la posizione attuale dell' ISS?(S/N): ").strip().lower()

    if posizione_now == "s":
        latitudine = (posizione["iss_position"]["latitude"])
        longitudine = (posizione["iss_position"]["longitude"])
        timestamp = (posizione["timestamp"])
        conversione_timestamp = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%d-%m-%Y %H:%M:%S')
        latitudine_1 = "Latitudine: {}"
        longitudine_1 = "Longitudine: {}"
        timestamp_1 = "Timestamp: {}"

        latitudine_2 = latitudine_1.format(latitudine)
        longitudine_2 = longitudine_1.format(longitudine)
        timestamp_2 = timestamp_1.format(conversione_timestamp)

        effetto(latitudine_2)
        effetto(longitudine_2)
        effetto(timestamp_2)
        break
    elif posizione_now == "n":
        uscita_3 = input("Desideri uscire dal programma?(S/N): ").strip().lower()
        if uscita_3 == "s":
            exit()
        elif uscita_3 == "n":
            break
    else:
        print("Per favore, inserire una risposta valida.")


# PREVISIONE POSIZIONE ISS DATA LA POSIZIONE UTENTE

while True:
    microtras()
    while True:
        previsione = input("Vuoi preveredere quando l'ISS orbiterà sopra di te?(S/N): ").strip().lower()
        microtras()

        if previsione == "s":
            permesso = input('''Per facilitare la ricerca della propria latitudine e longitudione
se si decide di continuare, verrà aperto il Browser e si verrà indirizzara su un sito
di ricerca. Bisognerà quindi inserire la propia località per trovare i due parameteri 
richiesti.
Continuare?(S/N)''')
            microtras()
            if permesso == "s":
                webbrowser.open('https://www.latlong.net/', new=2, )
                break
            elif permesso == "n":
                break
        elif previsione == "n":
            exit()
    while True:
        lat = float(input("Inserire la propria latitudine: "))
        long = float(input("Inserire la propria longitudine: "))

        parameters = {}

        parameters["lat"] = lat
        parameters["lon"] = long

        response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        posizione = response.json()

        microtras()

        print("Di seguito le prossime 5 previsioni in cui sarà possibile osservare l'ISS orbitare sopra di te ;)")
        microtras()
        for x in range(len(posizione["response"])):
            durata = (posizione["response"][x]["duration"])
            data = (posizione["response"][x]["risetime"])
            conversione_data = datetime.datetime.fromtimestamp(int(data)).strftime('%d-%m-%Y %H:%M:%S')
            risultato = "L'ISS sarà visibile, considerata la tua posizione il {}, e sarà osservabile per {} secondi"
            final = risultato.format(conversione_data, durata)

            effetto(final)

        break
    break
print("")
print("")
print("")
input("Premere invio per uscire dal programma.....")
exit()
