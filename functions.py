# Demonstration von Funktionen
# 01.11.2018, elo

def add(value1:int, value2:int) -> int:
    result = value1 + value2
    return result

def mul(value1:int, value2:int) -> int:
    pass

a : int = 1
b : int = 2
c : int = add(a, b)
print(c)
print(add(a, b))