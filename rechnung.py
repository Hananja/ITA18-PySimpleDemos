total: float = 0.0

done: bool = False
while not done:
    artno: str = input("Artikelnummer: ")
    count: int = int(input("Anzahl: "))
    price: float = float(input("Preis: "))
    total = total + count * price

    loop = input("Weitere Eingabe (J/N)? ")
    done = loop != "J" and loop != "j"

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