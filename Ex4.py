def a():
    x=int(input("x?"))
    i=1
    f=1
    while i < x+1:
        f*=i
        i+=1
    print(f"{x} factioriel vaut {f}")

def b():
    x = int(input("x?"))
    f = 1
    for i in range(1,x+1):
        f*=i
    print(f"{x} factioriel vaut {f}")

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