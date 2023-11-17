import re
num_format = re.compile(r"^\-?[0-9][0-9]*$")

def verif(X):
    if re.match(num_format, X):
        return X
    else:
        return 0
def a():
    n=int(verif(input("Nombre entier positif n?")))
    for i in range(n,-1,-1):
        print(i)
def b():
    n=int(verif(input("Nombre entier positif n?")))
    while n>=0:
        print(n)
        n-=1

while True:
    test=input("Quelle programme (a,b) ?")
    match test:
        case 'a':
            a()
        case 'b':
            b()
        case _:
            print("Inconnu!")
    print("--- \n")