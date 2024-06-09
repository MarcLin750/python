nbrTour = 0
n = 1
res = 0

print("Entrer un nombre pour cacluler approximativement son sinus: ", end='')
data = float(input())

while True:
    fact = 1
    rad = data**n
    for i in range(2, n+1):
        fact = fact * i

    if nbrTour%2 == 0:
        res = res + rad / fact
    else:
        res = res - rad / fact
    
    if nbrTour == 10:
        break

    nbrTour += 1
    n += 2

print(res)