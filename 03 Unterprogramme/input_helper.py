from typing import Union


def input_user_bool(prompt:str) -> bool:
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

def input_number(prompt:str, fraction:bool) -> Union[float, int]:
    """
    Display prompt and read number as int or float from user and return it.

    :param prompt: Text to display to the user.
    :param fraction: True for float and False for int input
    :return: Number entered by user
    """
    done: bool = False
    while not done:
        user_input = input(prompt)
        if fraction:
            # FIXME: check for valid float input
            return float(user_input)
        else:
            if user_input.isdecimal():
                return int(user_input)
            else:
                print("Fehler: keine ganze Zahl eingegeben")
