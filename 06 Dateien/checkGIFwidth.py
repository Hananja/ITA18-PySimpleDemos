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

    # Breite und Höhe bestimmen
    infile.seek(6) # Position 6 anwählen (Cursor setzen)
    width_data = infile.read(2) # 2 Bytes lesen
    width = width_data[0] + width_data[1] * 256
    print("Breite:", width)
    height_data = infile.read(2)
    height = height_data[0] + 256 * height_data[1]
    print("Höhe: ", height)
