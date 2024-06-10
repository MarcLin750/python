# Dois afficher une pyramide en fonction du nombre de ligne donnée par un chiffre
pyramide = ''
nbr = ''
part1 = 0
part2 = 0

n = int(input("Entrer la taille de la pyrapide (en ligne): "))

for i in range(n):
    espace = ' ' * (n - i - 1)

    for j in range(i+1):
        part1 = i+j+1
        unitePart1 = part1 % 10
        nbr += str(unitePart1)
    for h in range(i):
        part2 = part1 - (h + 1)
        unitePart2 = part2 % 10
        nbr += str(unitePart2)

    pyramide += espace + nbr + '\n'
    nbr = ''
    part1 = 0
    part2 = 0
    
print('\n')
print(pyramide)