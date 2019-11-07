# while 1:
#     euro = input("valoare euro pt conversie")
#     if euro.isdigit():
#         euro = int(euro)
#         print("valoarea convertita este: ", euro * 4.7, "RON")
#     else:
#         print("valoarea nu este numar")
#
#     quit = input("Apasa q pentru a iesi si orice tasta pentru a repeta conversia")
#     if quit.upper() == "Q":
#         break
#     else:
#         pass

for variabilaTemporar in range(0, 50, 5): # range(start, final, nr adaugat) 50 este luat <50
    print(variabilaTemporar)

for var in "abcde": # string-urile sunt siruri
    print(var)

string = "sir de caracter"
print(f"string.split(' ') => {string.split(' ')}")
#string[0] = "2" # string-urile nu se pot schimba

# tuple
# tuplele nu sunt mutabile
x = () # tupla goala
coordonateXYZ = (3, 4, 5)
print(f"doua duple concatenate {coordonateXYZ + (3, 2, 1)} ta-da")

inventar = None # None este echivalent a null
if not inventar:
    print("Momentan nu e nimic in inventar")

inventar = ("apa", "paie", "bataie")

print(f"\n Tuplul inventar este acum:{inventar}")

for item, value in enumerate(inventar):
    print(f"Produs {item} => {value}")

# liste
# listele sunt mutabile
list = [1, 2, 3, "Google", [4, 5, 6]]
print(list)
list[0] = "Salut"
print(list)

# append(value) adauga la finalul listei
# sort

l = [9, 4, 3, 2, 1, 0]
# sorted(sorted(l)) returneaza o copie sortata a listei
# print(l.sort) sorteaza si modifica array-ul initial

print(l[:])
print(l[:2]) # pana la indexul 2 (<l[2]) aka 9
print(l[::2]) # din 2 in 2 pornind de la indexul 0

# set
# datele sunt unice
# nu suporta indexarea
s = {1, 3, 9, 13} # empty set
print(f"Tipul este{type(s)}")
s.add(10)
s.discard(1)
s.add(3)
print(s, f"element 10 in lista: {3 in s}")
s2 = {2, 5, 8, 3, 9}
# & intersectie
# | uniune
# - diferenta
# ^ diferenta simetrica
print(s & s2, s | s2, s - s2, s ^ s2)

# dictionar
# practic hash map
# key poate fi doar numar sau string
# are proprietatea de mutabilitate
dict = {
    1:"abcd",
    "stringToInt": 10
}
dict.get("stringToInt", 5) # 5 este optional; daca "stringToInt" nu exista, atunci se returneaza 5

for k, v in dict.iteritems(): # iteritems() returneaza un iterator la dictionar (50% mai putina memorie folosita
    print(k, v)               # items() returneaza valorile din dictionar