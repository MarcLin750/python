print("Ce programme permet de vérifié si l'écureil peut attraper la noisette sur une roue numéroté de 0 à 99.")
print("Entrer le nombre de saut: ", end="")
saut = int(input())
print("Entrer la position de la noisette: ", end="")
position_cible = int(input())
position_courante = 0

while position_cible != position_courante:
    position_courante = position_courante + saut
    if position_courante >= 100:
        position_courante = position_courante % 100

    if position_cible == position_courante:
        print("Cible atteinte")
        break
    elif position_courante == 0:
        print(position_courante)
        print("Pas trouvée")
        break
    else:
        print(position_courante)
    