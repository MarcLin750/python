print("Entrée un nombre pour définir combien de nombre vous voulez additionner.\nOu entrée '-1' pour un nombre indéfini, le caractère 'F' mettra fin a l'addition.")
nbrTour = input()
res=0

if nbrTour == '-1':
    while True:
        data = input()
        if data == 'F':
            break
        n = int(data)
        res = res + n
else:
    for i in range(int(nbrTour)):
        data = input()
        n = int(data)
        res = res + n
print(res)