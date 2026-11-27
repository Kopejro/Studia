# Zadanie 1

punkty = int(input("Ile zdobyłeś punktów:"))
if punkty >= 80:
    print("Zaliczyłeś egzamin w terminie 0")
elif 50 < punkty <= 80:(
    print("Możesz poprawić jego wynik"))
else:
    print("Musisz poprawic wynik")



# Zadanie 2

x = float(input("Podaj x:"))
y = float(input("Podaj y:"))
z = float(input("Podaj z:"))
if x > y:
   x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(f"Liczby w kolejności rosnącej: {x}, {y}, {z}")



# Zadanie 3

Nazwa_pliku = 'Raport_maj.xlsx'
if Nazwa_pliku.endswith('xlsx'):
    print("Tak")
else:
    print("Nie")



# Zadanie 4

gol = int(input("Liczba strzelonych bramek: "))
bonus = 0


if gol >= 5:
    bonus += 5
    if gol > 10:
        bonus += 10

wynik = gol * 10 + bonus
print(f"Całkowity wynik drużyny: {wynik}")



# Zadanie 5

# A
with open("notowania_gieldowe.txt", "r") as plik:
    print(plik.read())

# B
with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")
with open("notowania_gieldowe.txt", "r") as plik:
    print(plik.read())



# Zadanie 6

while True:
    litera = input("Podaj literę: ")

    if len(litera) == 1 and litera.isalpha():
        break
    else:
        print("Nieprawidłowy format. Wpisz tylko jedną literę!")
        

if litera.isupper():
    print("To jest duża litera")
else:
    print("To jest mała litera")



# Zadanie 7

Hasło = 'pk47!jy0893'

if len(Hasło) >= 11 and "!" in Hasło:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")



# Zadanie 8

text = 'Studiuje-Informatykę'

pierwsze_trzy_znaki = text[0:3]
ostatnie_dwa_znaki = text[-2:]
print(pierwsze_trzy_znaki)
print(ostatnie_dwa_znaki)



# Zadanie 9

text = input("Podaj tekst z dużymi i małymi literami: ")
zamiana = text.swapcase()

print("Tekst po zamianie dużych liter na małe i małych na duże: ", zamiana)