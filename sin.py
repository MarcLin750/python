
n = 1
res = 0

print("Entrer un nombre pour cacluler approximativement son sinus: ", end='')
data = float(input())

for j in range(12):
    fact = 1
    rad = data**n
    for i in range(2, n+1):
        fact = fact * i

    if j%2 == 0:
        res = res + rad / fact
    else:
        res = res - rad / fact

    n += 2

print(res)