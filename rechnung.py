
def ask_user_bool(prompt:str) -> bool:
    "Query user input: yes or no and returns bool."
    done: bool = False
    while not done: # end by return
        user_input = input(prompt + " (J/N) ").upper()
        if user_input == "N":
            result = False
            done = True
        elif user_input == "J":
            result = True
            done = True
        else:
            print("Bitte J oder N eingeben! ")
    return result

def invoice():
    total: float = 0.0

    done: bool = False
    while not done:
        artno: str = input("Artikelnummer: ")
        count: int = int(input("Anzahl: "))
        price: float = float(input("Preis: "))
        total = total + count * price

        done = ask_user_bool("Eingabe beenden?")

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
    new_invoice = ask_user_bool("Weitere Rechnung?")