
def tri_bulle(tab):
    n = len(tab)

    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

print(tri_bulle([98, 22, 15, 32, 2, 74, 63, 70]))