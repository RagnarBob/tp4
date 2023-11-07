import random
import string

print("******************PATI CHENN*******************")
print("nimewo 1 :")
chenn = "King Ragnar"
print(chenn.lower(), "\n")

print("nimewo 2 :")
var = "ayibobo ayiti"
print(var.split(), "\n")

print("nimewo 3 :")  # nimewo 3
let = "the king ragnar"
print(let.title(), "\n")

print("nimewo 4 :")  # nimewo 4
chenn_nan = "mwen se yon Viking"
varyab = chenn_nan.split()
new_chenn = ""
for el in varyab:
    new_chenn += el[0]
print(new_chenn, "\n")

print("nimewo 5 :")  # nimewo 5
karak = "madame"
print(karak.replace("a", "@"), "\n")

print("nimewo 6 :")  # nimewo 6
vvar = "ThamArt"
vvar_inv = vvar[::-1]
print(vvar_inv.upper(), "\n")

print("nimewo 7 :")  # nimewo 7
indexo = "Elle est mignone"
ver = indexo.index("e")
print(ver, "\n")

print("nimewo 8 :")  # nimewo 8
chaine = "Elle est une amie speciale et je l'aime"
cpt = 0
for karak in chaine:
    if karak == "e":
        cpt += 1
print("kantite (e) ki genyen an se:", cpt, "\n")

print("nimewo 9 :")  # numewo 9
hello = "Ayiti kapab avanse"
yes = 0
liste = []
for kar in hello:
    if kar == "a":
        liste.append(str(yes))
    yes += 1
# soti = " , ".join(liste)
print(liste, "\n")

print("nimewo 10 :")  # nimewo 10
bob = "je suis Ragnar Bob the king"
king = bob.replace(" ", "")
doll = len(king)
ragnar = str(doll)
print(king+ragnar+"\n")

print("****************PATI LIS*****************")
print("nimewo 1 :")
n = 20
liss = []
for i in range(n+1):
    if i % 2 == 0:
        liss.append(i)
print(liss)

print("nimewo 2 :")
lis_antye = [1, 2, 3, 4, 5, 6, 7]
lis_chenn = list(map(str, lis_antye))
print(lis_chenn)

print("nimewo 3 :")
list_miniskil = ["king", "ragnar", "bob"]
list_majiskil = [el.upper() for el in list_miniskil]
print(list_majiskil)

print("nimewo 4 :")
li = [2, 3, 4, 5, 6, 9, 12, 15, 18, 19, 22, 34, 33, 60]
new_list = [li[i] for i in range(0, len(li), 3)]
print(new_list)

print("nimewo 5:")
list_group = [2, 3, 4, 5, 20, 40, 46, 48, 50]
new_list_group = [tuple(list_group[i:i+3])
                  for i in range(0, len(list_group), 3)]
print(new_list_group)

print("nimewo 6:")
list_doublon = [1, 2, 3, 2, 3, 4, 4, 4, 5, 6, 6, 7, 2]
lis_san_doublon = list(set(list_doublon))
print(lis_san_doublon)

print("nimewo 7:")
list_1 = [1, 2, 4, 5, 6, 7, 8]
list_2 = [1, 5, 3, 9, 10, 12]
list_commun = list(set(list_1) & set(list_2))
print(list_commun)

print("nimewo 8:")
list_1 = [1, 2, 4, 5, 6, 7, 8]
list_2 = [1, 5, 3, 9, 10, 12]
nouvo_liste = list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))
print(nouvo_liste)

print("nimewo 9:")
dicto = {'bob': '4', 'ragnar': '6'}
kle = list(dicto.keys())
vale = list(dicto.values())
print(kle)
print(vale)

print("nimewo 10:")
list_1 = [1, 2, 4, 5, 6, 7, 8]
list_2 = [1, 5, 3, 9, 10, 12]
list_3 = [2, 3, 4, 5, 12, 14]
reunion = set(list_1) | set(list_2) | set(list_3)
new_liste = list(reunion)
print(new_liste, "\n")

print("****************PATI dict*****************")
print("nimewo 1:")
dictio = {'king': 'ragnar', 'bob': 'doll'}
valeur = list(dictio.values())
print(valeur)

print("nimewo 2:")
user = input("antre yon bgy :")
if user.startswith("{") and user.endswith("}"):
    print("saw antre an gen akolad ni devan ni deye")
else:
    print("li pa gen akolad ni devan ni deye") 

print("nimewo 3:")
dik = {'the': 'king', 'bob': 'ragnar'}
for key in dik.keys():
    print(key)

print("nimewo 4:")
dikk = {'the': 'king', 'bob': 'ragnar'}
for valeur in dikk.values():
    print(valeur)

print("nimewo 5:")
diks = {'the': 'king', 'bob': 'ragnar'}
kopi_diks = diks.copy()
print(kopi_diks)

print("nimewo 6:")
dic = {'the': 'king', 'bob': 'ragnar', 'doll': 12, "maken": 34}
nouvo_dict = {key: ("_" + vale if isinstance(vale, str) else vale)
              for key, vale in dic.items()}
print(nouvo_dict)

print("nimewo 7:")
dictt = {'the': '2', 'bob': '3', 'doll': 'bob', "maken": 'king'}
new_dict = {kle: valeu for kle, valeu in dictt.items() if valeu.isdigit()}
print(new_dict)

print("nimewo 8:")
dicttt = {'the': '2', 'bob': '3', 'doll': 'bob', "maken": 'king'}
tipl = list(dicttt.items())
print(tipl)

print("nimewo 9:")
ti = ("a", 2), ("b", 3), ("d", 8), ("e", 7)
e = dict(ti)
print(e)

print("nimewo 10:")
d1 = {'a':'king','b':'ragnar','c':10,'d':30}
d2 = {'a':'2','f':'king','c':10,"h":6}
diict = {}
for kle in d1.keys() | d2.keys():
    val = d1.get(kle,'')
    val1 = d2.get(kle,'')
    if isinstance(val,int) and isinstance(val1,int):
        diict[kle] = val + val1
    elif isinstance(val,str) and isinstance(val1,str):
        diict[kle] = val + val1
    elif isinstance(val,list) and isinstance(val1,list):
        diict[kle] = val + val1
    elif isinstance(val,set) and isinstance(val1,set):
        diict[kle] = val + val1    
    else:
        diict[kle] = str(val) + str(val1)        
print(diict)

print("****************PATI FONCTION*****************")
print("nimewo 1:")
def retounen(mo):
    inves = mo[::-1]
    return inves
inverse = retounen("doll")
print(inverse)

print("nimewo 2:")
def jenere (n):
    kod = ''.join(random.choice(string.ascii_letters) for _ in range(n))
    return kod
n = 10 
kod_aleyatwa = jenere(n)
print(kod_aleyatwa)

print("nimewo 3:")
def aleatwa(n):
    karakte = string.ascii_letters
    kood = ''.join(random.sample(karakte,n))
    return kood
n = 10
ko_ale = aleatwa(n)
print(ko_ale)

print("nimewo 4:")
def aleat(n):
    alphanumerik = string.ascii_letters + string.digits
    num = ''.join(random.choice(alphanumerik) for _ in range(n))
    return num
n = 10 
nime = aleat(n)
print(nime)

print("nimewo 5:")
def je_slug(chaine):
    slug = ''.join(char if char.isalnum() or char == '-' else '' for char in chaine)
    slug = slug.strip('-')
    return slug
chaine = "hi, wey! 178"
slug = je_slug(chaine)
print(slug)

print("nimewo 6:")
def separ(moo):
    separe = ','.join(moo)
    return separe
name = "Thamie"
sepa = separ(name)
print(sepa)


print("nimewo 7:")
def kripte_mo(mo,alfabe):
    mokripte = [str(alfabe.index(caractere)) for caractere in mo if caractere in alfabe ]
    mokripte = '-'.join(mokripte)
    return mokripte
alfabe = string.ascii_letters
mo = kripte_mo("THAMIE",alfabe)
print(mo)

print("nimewo 8:")
def dekripte(mokrpte,alfabe):
    position_let = [int(position) for position in mokrpte.split("-")]
    modekripte = ''.join([alfabe[position] for position in position_let] )
    return modekripte
mokrpte = "45-33-26-38-34-30"
alfabe = string.ascii_letters
mot = dekripte(mokrpte,alfabe)
print(mot)

print("nimewo 9:")
def retour(v1,v2):
    v1,v2 = v2,v1
    return v1,v2
v1=23
v2 ="king"
v1,v2=retour(v1,v2)
print(v1,v2)

print("nimewo 10:")
def inisyal(nom):
    ini= ""
    nonsplit=nom.split("-")
    for el in nonsplit:
        namesplit = el.split()
        for el in namesplit:
            ini += el[0]
    return ini
nonm = "alexis-makendy bob"
initial = ' '.join(inisyal(nonm))
print(initial)
