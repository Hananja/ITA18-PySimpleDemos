from input_helper import input_user_bool


def invoice():
    total: float = 0.0

    done: bool = False
    while not done:
        artno: str = input("Artikelnummer: ")
        count: int = int(input("Anzahl: "))
        price: float = float(input("Preis: "))
        total = total + count * price

        done = input_user_bool("Eingabe beenden?")

    tax_rate = 0.19
    tax = total * tax_rate
    gross = total + tax

    free_shipping_limit = 50
    if gross < free_shipping_limit:
        shipping = 7.5
        print("Porto: " + str(shipping))
        gross = gross + shipping

    print( "Steuer: " + str(tax))
    print( "Netto: " + str(total))
    print("Brutto: " + str(gross))

new_invoice = True
while new_invoice:
    invoice()
    new_invoice = input_user_bool("Weitere Rechnung?")
