# SpaceNews

Informazioni live su astronauti e la Stazione Spaziale Internazionale

# ToDo
Combinare le funzioni:

```python
def delay(testo):
    for x in testo:
        print(x, end="")
        sys.stdout.flush()
        sleep(0.01)
    print("")

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

