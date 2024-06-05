import random
nbrEssaisMax = 6
secret = random.randint(0, 100)

print("Trouve le nombre secret, avec 6 essais.")

for i in range(nbrEssaisMax):
    n = int(input())
    
    if i == 5:
        break
    elif n == secret:
        break
    elif n > secret:
        print("Trop grand")
    else:
        print("Trop petit")

if n != secret:
    print("Perdu ! Le secret était", secret)
else:
    print("Gagné en",i+1,"essai(s) !")