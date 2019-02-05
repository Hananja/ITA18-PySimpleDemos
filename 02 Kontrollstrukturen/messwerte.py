new_row: bool = True
while new_row:
    count: int = 0
    sum: float = 0.0

    new_value: bool = True
    while new_value:
        value: float = float(input("Messwert: "))
        if value >= 0:
            count += 1
            sum += value
        else:
            print("Fehler: die Zahl ist < 0")

        user_input = input("Weiterer Messwert (J/N)? ")
        new_value = user_input.upper() == 'J'

    print("Anzahl: " + str(count))
    print("Summe: %0.4f" % sum)
    print("Mittelwert: " + str(sum/count))

    new_row = "J" == input("Weitere Messreihe? (J/N) ").upper()