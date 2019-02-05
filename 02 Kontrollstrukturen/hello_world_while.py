# Demonstration von Schleifen am Beispiel
# Hello World
# Autor: E. Loos
# Datum: 19.09.2018

# Eingabe
name = input("Bitte Name eingeben: ")
sex = None
while sex != 'm' and sex != 'w': # bis richtige Eingabe gelesen wurde
    sex = input("Bitte Geschlecht eingeben (m/w): ")

# Verarbeitung
if sex == 'm':
    greeting = "Herr"
elif sex == 'w':
    greeting = 'Frau'
else:
    greeting = None # Fehler, sollte nicht passieren

# Ausgabe
print("Hallo " + greeting + " " + name)
