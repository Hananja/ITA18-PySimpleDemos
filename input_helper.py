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
