# SpaceNews

Informazioni live su astronauti e la Stazione Spaziale Internazionale

# ToDo
Combinare le funzioni:

```python

# Ritardo tesro, effetto digitazione

def delay(testo):
    for x in testo:
        print(x, end="")
        sys.stdout.flush()
        sleep(0.01)
    print("")
```
```python

# Riquadro asterischi stringa

def effetto(testo):
    print("")
    for x in testo:
        print("#", end="")
    print("")
    print(testo)

    for x in testo:
        print("#", end="")
    print("")
```

