print("Entrer un nombre pour voir sa table de multiplication avec ceux qui le précèdent: ", end='')
n = int(input())
somme = 0

for i in range(n):
    for j in range(n):
        somme = (i + 1) * (j + 1)
        res = ' ' + str(somme) + ' '
        print(res, end=' ')
        somme = 0
    print('')