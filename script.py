
def exo_1(a, b, c = 12):
    tmp = a
    a = c
    c = b
    b = tmp
    """
1) toutes les variables de la fonction supprimées à la sortie de la fonction

2) mettre des variables dans return permet de sortir LA VALEUR de variables avant
qu'elles soient supprimées

3) return coupe l'exécution de la fonction
    """
    return a, b, c

x, y, z = exo_1(1, 2, 3)
print(f"x = {x}, y = {y}, z = {z}")

x, y , z = exo_1(5, 4)
print(f"x = {x}, y = {y}, z = {z}")


t = 10
p = 3.15
print(f"t = {t}, p = {p}")

# Les LISTES
klobatildo = [1, 4, 9]
klobatildo[0] = 5 # Premier élément est 0
klobatildo[len(klobatildo) - 1] = 6

klobatildo.append(7) # Ajout à une liste

terrifiant = [
    [
        [
            [
                [4, 4]
            ],
            ["dfgdfg"]
        ]
    ]
]

# Les DICTIONNAIRES
greg = {
    "Gregory" : {
        "age" : 12,
        "espérance de vie" : -14,
    },
    "Blikomto" : 45,
    "Madoka" : 34,
    "Subaru" : 256,
}

print(greg)
print(f"Gregory a {greg['Gregory']['age']} ans")

# Les BOUCLES
x = 0

for i in range(12): # range(début, fin, pas)
    x += 1 # Applique "x+1" 12 fois

for i in range(4): # range(4) = [0, 1, 2, 3]
    print(i)

for i in klobatildo:
    x += 1

for i in [4, 12, 34, 5]:
    x += 1

for i in [4, 12, 34, 5]:
    print(i)

for i in greg.keys():
    x += 1

for k, v in greg.items():
    x += 1

while x > 0:
    x -= 1

"""
Opérateurs
x += 1 <=> x = x+1
x -= 1 <=> x = x-1
x *= 1 <=> x = x*1
x /= 1 <=> x = x/1

x %= 1 <=> x = x%1

Explication division euclidienne

13 = 4 * 3 + 1

13 / 4 = 3.25
13 // 4 = 3
13 % 4 = 1

Transformer chaine de charactères en liste
"Rem".list <=> ['R', 'e', 'm']

Conditions
if a == b:
if a > b:
if a < b:
if a != b:
if a >= b:
if a <= b:

if a in liste:
if a not in liste:

if a == b or a > b:
if a == b and a < b:

if X:
    executé que si X vrai
elif Y:
    executé que si X faux ET Y vrai
else:
    executé que si X faux ET Y faux

match X:
    case 1:
        bla
    case 2:
        blad
    case 3:
        blag
    case 4:
        blasq
    case 5:
        blaz

len et range
len(liste) -> nombre d'éléments de la liste
range(nombre d'éléments de la liste) -> liste de nombres croissants commençant par 0

exemple:
len([1, 7, 4]) -> 3
range(3) -> [0, 1, 2]

min et max:
min(a, b) -> valeur la plus petite entre a et b
max(a, b) -> valeur la plus grande entre a et b


Rem
Ram
R m

Rem
Ramistratose
R m

Blopirto
Hooplito
  o

Opérateur ternaire :
x = 0
if A:
    x = 1
else:
    x = 2

x = 1 if A else 2
"""

def get_intersection(str_1, str_2):
    str_1_list = list(str_1)
    str_2_list = list(str_2)

    intersection = ""
    for i in range(
        min(
            len(str_1_list),
            len(str_2_list)
        )
    ):
        if str_1_list[i] == str_2_list[i]:
            intersection += str_1_list[i]
        # else:
        #     intersection += " "
    return intersection

def exo_3():
    var_1 = input("Nom 1: ")
    var_2 = input("Nom 2: ")

    var_1 = var_1.lower()
    var_2 = var_2.lower()

    print(get_intersection(var_1, var_2))

exo_3()

"""
Exo 3:
1) Comparer la longueur des 2 et prendre le plus court
2) Comparer les lettres une par une
3) Ressortir les lettres en commun à la même place

1) 
Trouver les longueurs des listes :
    len(str_1_list)
    len(str_2_list)
Comparer ces longueurs :
    min(...)

2)
Comparer les lettres :
    if str_1_list[i] == str_2_list[i]:
une par une :
    for i in range(...):
    

"""
