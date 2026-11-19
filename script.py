"""imie = input("Enter imie: ")
x = "Cześć", imie
print(x)"""


# Zadanie 1

# A)
x = 1 +2 #dodawanie
print(type(x))

x = 1 + 4.5 #dodawanie
print(type(x))

x = 3 / 2 #dzielenie
print(type(x))

x = 4 / 2 #dzielenie
print(type(x))

x = 3 // 2 #dzielenie całkowite
print(type(x))

x = -3 // 2 #dzielenie całkowite
print(type(x))

x = 11 % 2 #reszta z dzielenia
print(type(x))

x = 2 ** 10 #potęgowanie
print(type(x))

x = 8 ** (1 / 3) #pierwiastek sześcienny
print(type(x))

# B)
"""
1. int(3.0) - zmieni liczbe na 3
2. float(3) - zmieni liczbe na 3.0
3. float("3") - zmieni str "3" na liczbe 3.0
4. str(12.4) - zmieni liczbe 12.4 na str "12.4"
5. bool(0) - zmieni 0 na False
"""


# Zadanie 2

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)


# Zadanie 3

imię = "Jan"
wiek = 20
wzrost = 178

print("Nazywam się", imię, "i mam", wiek, "lat.")
print("Mój wzrost to", wzrost, "cm.")


# Zadanie 4

Cena = 39.99
Rabat = 0.2 # rabat 20%

print(f"Cena po rabacie wynosi: {Cena * (1 - Rabat):.2f} PLN")


# Zadanie 5

a = 5
b = 3

pole = a * b
obwod = 2 * (a + b)

print(f"Pole prostokąta wynosi: {pole}")
print(f"Obwód prostokąta wynosi: {obwod}")


# Zadanie 6

pokonane_kilometry = float(input("Podaj liczbę pokonanych kilometrów: "))
srednie_spalanie = float(input("Podaj średnie spalanie (l/100km): "))

print(f"Przewidywane zużycie paliwa wynosi: {pokonane_kilometry * srednie_spalanie / 100:.2f} litrów")
print(f"Szacowany koszt podróży przy cenie paliwa 6,50 zł/l wynosi: {pokonane_kilometry * srednie_spalanie / 100 * 6.50:.2f} zł")


# A)

import random
pokonane_kilometry = random.randint(10, 5000)
srednie_spalanie = float(input("Podaj średnie spalanie (l/100km): "))
cena_paliwa = float(input("Podaj cenę paliwa (zł/l): "))

print(f"Przewidywane zużycie paliwa po pokonaniu {pokonane_kilometry} km wynosi: {pokonane_kilometry * srednie_spalanie / 100:.2f} litrów")
print(f"Szacowany koszt podróży przy pokonaniu {pokonane_kilometry} km i cenie paliwa {cena_paliwa:.2f} zł/l wynosi: {pokonane_kilometry * srednie_spalanie / 100 * cena_paliwa:.2f} zł")


# Zadanie 7

print("Rozwiązywanie równania liniowego ax + b = 0 ")

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))

if a != 0:
    x = -b / a
    print(f"Równanie ma jedno rozwiązanie: x = {x}")

if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie nie ma rozwiązania.")


# Zadanie 8

print("Rozwiązywanie równania kwadratowego ax^2 + bx + c = 0")

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

if a == 0:
    print("To nie jest równanie kwadratowe.")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)

        print(f"Równanie ma dwa rozwiązania: x1 = {x1}, x2 = {x2}")

    elif delta == 0:
        x = -b / (2*a)
        print(f"Równanie ma jedno rozwiązanie: x = {x}")

    else:
        print("Równanie nie ma rozwiązań rzeczywistych.")


# Zadanie 9

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

dodawanie = a + b
odejmowanie = a - b
mnożenie = a * b
dzielenie = a / b if b != 0 else "Nie można dzielić przez zero"
mnożenie = a * b
potęgowanie = a ** b

print(f"dodawanie: {dodawanie}")
print(f"odejmowanie: {odejmowanie}")
print(f"mnożenie: {mnożenie}")
print(f"dzielenie: {dzielenie}")
print(f"potęgowanie: {potęgowanie}")
