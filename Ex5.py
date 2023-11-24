import re

num_format = re.compile(r"^\-?[0-9][0-9]*$")
h1, h2=-1, -1
cost,t1,t2=0,0,0

def verif(x):
    while True:
        if not (re.match(num_format, x)):
            print("Valeur incorrect!")
            return -1
        else:
            x=int(x)
            if x>=0 and x<=24:
                return x
            else:
                print("Valeur incorrect!")
                return -1

while h1==-1:
    h1=input("Donnez l’heure de début de la location (un entier) : ")
    h1=int(verif(h1))
while h2==-1:
    h2=input("Donnez l’heure de fin de la location (un entier) : ")
    h2=int(verif(h2))
print("Vous avez loué votre vélo pendant")

for i in range(h1,h2):
    if i>=7 and i<17:
        t2+=1
        cost+=2
    else:
        t1+=1
        cost+=1

print(f"{t1} heure(s) au tarif horaire de 1.0 euro(s)")
print(f"{t2} heure(s) au tarif horaire de 2.0 euro(s)")
print(f"Le montant total à payer est de {cost}.0 euro(s).")




