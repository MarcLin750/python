print("Entrée un nombre qui détéerminera la taille du triable droit: ", end='')

n = int(input())
espace = ' '
x = 'X'
res = ''

for i in range(0, n, +1):
    res = espace*i + x*(n-i)
    print(res , end='\n')