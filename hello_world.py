# -*- coding: cp1252 -*-

# Eingabe
# -------
# Die Variable name wird angelegt
# mit dem Datentyp str (Zeichenkette)
# und der Wert zugewiesen, der von input(...)
# zur�ckgegeben wird.
# Die Funktion input(...) lie�t eine Zeichenkette
# von der Konsole vom Nutzer ein und gibt diese zur�ck.
name : str = input("Bitte Name eingeben: ")

# Verarbeitung
# ------------
# Die Variable greeting wird angelegt mit dem Datentyp str
# und eine zusammengesetze Begr��ungsformel wird der
# Variable zugewiesen
greeting : str = "Hello " + name + "!" # + h�ngt Zeichenketten aneinander

# Ausgabe
# -------
# Die Funktion print(...) gibt den Inhalt
# der Variable greeting auf der Konsole aus
print(greeting)
