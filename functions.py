# Demonstration von Funktionen
# 01.11.2018, elo

# Addition
def add(value1:int, value2:int) -> int:
    result = value1 + value2
    return result

# Multiplikation
def mul(value1:int, value2:int) -> int:
    result = 0
    while value1 > 0:
        result = add(result, value2)  # addiert value2 zu result
        value1 = value1 - 1           # verkleinert um 1
    return result

a : int = 1
b : int = 2
print(add(a, b))
c : int = 3
print(mul(c, 5))