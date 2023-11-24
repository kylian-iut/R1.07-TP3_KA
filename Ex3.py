import random

while True:
    k=random.randint(0,100)
    i=1
    while True:
        x=int(input("x?"))
        if x > k:
            print("Plus petit")
        elif x < k:
            print("Plus grand")
        else:
            print(f"Trouvé en {i} itération.")
            break
        i+=1
    print("---")
