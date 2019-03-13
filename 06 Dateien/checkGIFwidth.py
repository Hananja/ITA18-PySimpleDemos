# Auf GIF Prüfen und Breite ausgeben
# Datum: 13.03.2019

with open("smiley.gif", "rb") as infile:
    magic = infile.read(4) # Anzahl: 4 Bytes
    print(magic)

    # erste Alternative
    if magic == b"GIF8":
        print("ein GIF File")
    else:
        print("kein GIF File")

    # zweite Alternative
    if magic.decode("ascii") == "GIF8": # unsicher, falls magic nicht dekodierbar
        print("ein GIF File")
    else:
        print("kein GIF File")

    # dritte alternative
    if magic == "GIF8".encode("ascii"):
        print("ein GIF File")
    else:
        print("kein GIF File")

    # Breite bestimmen
    # TODO