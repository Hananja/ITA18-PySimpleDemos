# Demonstration von bedingten Verzweigungen am Beispiel
# Hello World
# Autor: E. Loos
# Datum: 19.09.2018

# Eingabe
name = input("Bitte Name eingeben: ")
sex  = input("Bitte Geschlecht eingeben (m/w): ")

# Verarbeitung
if sex == 'm':
    greeting = "Herr"
else:
    if sex == 'w':
        greeting = 'Frau'
    else:
        greeting = 'Herr/Frau'

# Ausgabe
print("Hallo " + greeting + " " + name)
