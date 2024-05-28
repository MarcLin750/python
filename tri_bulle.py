
# fonction du nom de tri_bulle
def tri_bulle(tab):

    # la variable n compte le nombre d'élément dans la variable tab grace à la fonction "len()"
    n = len(tab)

    # boucle for qui se répète tant que la variable i n'est pas égal à n (tout les deux des variables de type nombre)
    for i in range(n):
        # boucle for j qui tri et intervertie les places du plus petit avec le plus grands en liste croissante
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
            # fin de la boucle j qui ajoute 1 à la bariable j
        # fin de la boucle for i et ajoute 1 à la variable i
    return tab

# affiche le résultat de la fronction tri_bulle avec comme paramètre une liste de nombre aléatoire
print(tri_bulle([98, 22, 15, 32, 2, 74, 63, 70]))
