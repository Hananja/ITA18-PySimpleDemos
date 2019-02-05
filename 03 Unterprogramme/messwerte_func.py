from input_helper import input_user_bool

def input_value() -> float:
    "read and return float value >=0 from user console"
    done: bool = False
    while not done:
        # TODO: handle wrong input
        user_input: str = input("Messwert: ")
        value: float = float(user_input)
        if value >= 0:
            return value
        else:
            print("Fehler: die Zahl ist < 0") # FIXME: Exception

def output_result(count, sum):
    "output count, sum and average with comments"
    print("Anzahl: " + str(count))
    print("Summe: %0.4f" % sum)
    print("Mittelwert: " + str(sum / count))

def handle_row():
    "input values, do calculation and output result"
    count: int = 0
    sum: float = 0.0

    new_value: bool = True
    while new_value:
        sum += input_value()
        count += 1
        new_value = input_user_bool("Weiterer Messwert")

    output_result(count, sum)

def main():
    "main program"
    new_row: bool = True
    while new_row:
        handle_row()
        new_row = input_user_bool("Weitere Messreihe?")

main()
