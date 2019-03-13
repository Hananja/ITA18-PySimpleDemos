# Zählen von Zeilen in einer Datei

with open("primes.txt") as f:
    lines = f.readlines()

    # Ausgabe der numerierten Zeilen:
    for linenumber, line in enumerate(lines):
        print(linenumber, line, end="")
    print() # Zeilenende

    # Ausgabe der Zeilenzahl:
    print("Anzahl der Zeilen:", len(lines))