import re
def a():
    N=int(input("N?"))
    for i in range(0,N+1):
        print(i)

def b():
    while True:
        if input("") == str(100):
            break

def c():
    num_format = re.compile(r"^\-?[0-9][0-9]*$")
    liste=[0]*3
    for i in range(0,10):
        while True:
            x=input(f"{i}?")
            if not(re.match(num_format, x)):
                print("Valeur incorrect!")
            else:
                x=int(x)
                if x>=0 and x<=20:
                    if x<10:
                        liste[0]+=1
                    if x>=10 and x<15:
                        liste[1]+=1
                    if x>=15:
                        liste[2]+=1
                    break
                else:
                    print("Valeur incorrect!")
    print(f"Il y a {liste[0]} valeur(s) <10")
    print(f"Il y a {liste[1]} valeur(s) entre 10 et 15 exclu")
    print(f"Il y a {liste[2]} valeur(s) >=15")

def d():
    X = int(input("N?"))
    N,Y=0,0
    while Y<X:
        N+=1
        Y+=N
    print(N)

while True:
    test=input("Quelle programme (a,b,c,d) ?")
    match test:
        case 'a':
            a()
        case 'b':
            b()
        case 'c':
            c()
        case 'd':
            d()
        case _:
            print("Inconnu!")
    print("--- \n")




