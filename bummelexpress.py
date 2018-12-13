# Umsetzung des Bummelexpress mit Unterprogrammen (Frunktionen)

# Um die Unterprogramme leichter in mehreren Programmen nutzen zu können,
# sind diese in eine andere Datei ausgelagert (siehe input_helper.py).
# Sie können in diesem Programm verwendet werden, wenn die Datei sich im
# gleichen Verzeichnis befindet und die Unterprogramme hier importiert werden.
from input_helper import input_user_bool, input_number

# Mögliche Aufteilung:
# - Preisberechung
# - Zuschläge
# - Ermäszigungen
#
# Alternativ könnte die Berechnung auch in einem Unterprogramm
# zusammengefasst werden.

# Benennung von Zahlen, um magische Nummern zu verhindern
tax_rate        = 0.19
express_fee     = 5.00
reservation_fee = 3.50
night_discount_rate = 0.15

def get_price(distance:float) -> float:
    "calculate and return base price according to distance"
    if distance < 100:
        price = 0.25
    elif distance <= 500:
        price = 0.2
    else:
        price = 0.15
    return price * distance

def get_additions(is_express: bool, do_reservation: bool) -> float:
    "calculate and return total of additions"
    addition = 0.0
    if is_express:
        addition += express_fee
    if do_reservation:
        addition += reservation_fee
    return addition

def get_discounts(is_night_ride: bool, single_price: float) -> float:
    "calculate and return total of discouunts"
    if is_night_ride:
        return single_price * night_discount_rate
    else:
        return 0.0

def output_result(net: float, tax: float, gross: float) -> None:
    "output restult to console"
    # FIXME: round output to cents
    print("Nettopreis:  " + str(net))
    print("Steuer:      " + str(tax))
    print("Bruttopreis: " + str(gross))

# Hauptfuktion
def main():
    # zu den Unterprogrammen: siehe Kommentar oben

    # input
    count          = input_number("Anzahl: ", False)
    distance       = input_number("Entfernung: ", True)
    is_express     = input_user_bool("Schnellexpress?")
    do_reservation = input_user_bool("Reservierung?")
    is_night_ride  = input_user_bool("Nachtfahrt?")

    # single price calculation
    single_price  = get_price(distance)
    single_price += get_additions(is_express, do_reservation)
    single_price -= get_discounts(is_night_ride, single_price)

    # final and tax calculation
    net   = count * single_price
    tax   = net * tax_rate
    gross = net + tax

    # output
    output_result(net, tax, gross)

while input_user_bool("weitere Fahrkarten berechnen?"):
    main()
