"""Moduł służący do obliczania obowdu i pola trójkąta oraz wskazania rodzaju trójkąta."""

import math


def check_condition_of_existing_triangle(a, b, c):
    sides = [a, b, c]
    longest_side = max(a, b, c)
    sides.remove(longest_side)
    if longest_side >= sides[0] + sides[1]:
        print("Trojkata nie mozna zbudowac")
        return False
    else:
        print("Trojkat mozna zbudowac")
        return True


def calculate_circuit(a, b, c):
    circuit = a + b + c
    print("Obwod trojkata wynosi: ", circuit)
    return circuit


def calculate_area(a, b, c):
    half_of_circuit = 0.5 * calculate_circuit(a, b, c)
    area = math.sqrt(half_of_circuit * (half_of_circuit - a) * (half_of_circuit - b) * (half_of_circuit - c))
    print("Pole trojkata wynosi: ", area)


def calculate_type_of_triangle(a, b, c):
    if a == b and b == c:
        print("Trojkat rownoboczny")
    elif a == b or a == c or b == c:
        print("Trojkat rownoramienny")
    elif a != b and b != c and c != a:
        print("Trojkat roznoboczny")


def calculate_type_of_triangle_based_on_angle(a, b, c):
    sides = [a, b, c]
    longest_side = max(a, b, c)
    sides.remove(longest_side)
    if pow(longest_side, 2) > pow(sides[0], 2) + pow(sides[1], 2):
        print("Trojkat rozwartokatny")
    elif pow(longest_side, 2) == pow(sides[0], 2) + pow(sides[1], 2):
        print("Trojkat prostokatny")
    elif pow(longest_side, 2) < pow(sides[0], 2) + pow(sides[1], 2):
        print("Trojkat ostrokatny")


