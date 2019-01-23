# Diverse Demonstrationen zur Verwendung von Listen
from typing import List, Any


# Aufgabe 1 a
def demo_prime_numbers():
    # Initialisierung
    primfaktoren = [2, 2, 3, 7]
    # Verarbeitung
    produkt = 1
    for element in primfaktoren:
        print(produkt * element, "=", produkt, "*", element)
        produkt = produkt * element
    # Ausgabe
    print("Primfaktoren:", primfaktoren)
    print('Zahl:', produkt)


def get_product(data: List[int]) -> int:
    product = 1
    for element in data:
        product *= element
    return product


def run_demo_prime_numbers():
    demo_prime_numbers()


# Aufgabe 1 b
def count_in_iteable(mylist: List[Any], number: Any) -> int:
    counter = 0
    for element in mylist:
        if element == number:
            counter += 1
    return counter


def run_count_in_iterable():
    mylist = [2, 2, 3, 3, 7, 2, 9, 5]
    number = 3
    print(count_in_iteable(mylist, number))
    print(mylist.count(number))


# Aufgabe 1 c
def calc_product_list(data: List[List[int]]) -> int:
    product = 1
    for item in data:
        for i in range(item[1]):
            product *= item[0]
    return product


def run_calc_produrct_list():
    print(calc_product_list([[2, 2], [3, 1], [5, 0], [7, 1]]))


# Aufgabe 1 d
def calc_histogramm(data: List[Any]):
    done_items = []
    result = []
    for item in data:
        if item not in done_items:
            # FIXME: hoch null fehlt noch
            done_items.append(item)
            result.append([item, data.count(item)])
    return result


def calc_full_histogram(data: List[Any], values: List[Any]):
    done_values = []
    for v in values:
        if v not in done_values:
            done_values.append(v)
            yield [v, data.count(v)]


def calc_prime_histogram(data: List[int]) -> List[List[int]]:
    prime_list = get_prime_list(max(data))
    return list(calc_full_histogram(data, prime_list))


def run_histogram():
    mylist = [2, 2, 3, 3, 7, 2, 7, 13]
    print(calc_histogramm(mylist))
    print(list(calc_prime_histogram(mylist)))


# Aufgabe 1 e
def get_prime_list(num: int) -> List[int]:
    for i in range(2, num + 1):
        is_prime = True
        for d in range(2, int(i / 2)):
            if i % d == 0:
                is_prime = False
                break
        if is_prime:
            yield i


def run_get_prime_list():
    print(get_prime_list(84))


# Hauptprogramm(e)
# run_demo_prime_numbers()
# run_count_in_iterable()
run_calc_produrct_list()
# run_histogram()
# run_get_prime_list()
