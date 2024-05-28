import msvcrt

l = []
vie = 10
mot = ''
pendu = []
proposition = ''

def saisie_securisee(prompt=''):
    """Masque les entrées utilisateur et affiche des étoiles"""
    motsecret = b'' 
    while True:
        caractere = msvcrt.getch()
        if caractere in b'\r\n':
            print('')
            break
        elif caractere == b'\x08':
            motsecret = motsecret[:-1]
            print('\r' + prompt + '*' * len(motsecret), end=' ')
        else:
            motsecret += caractere
            print('*', end='', flush=True)
    return motsecret.decode('utf-8')

def enregistre_mot(motsecret, n):
    for i in motsecret:
        pendu.append(motsecret[n])
        n += 1

def affiche_motsecret(pendu, n):
    for c in pendu:
        if c.isalpha():
            n += 1
    print("Il y a",n,"letres.\n")

def devinette(pendu, proposition, a, l):
    
    print("[", end=' ')
    for c in pendu:
        if c == proposition or c in l :
            print(c, end=' ')
            a += 1
        elif c.isalpha():
            print('_', end=' ')
        else:
            print(c, end=' ')
            a += 1
    print("]\n")

    return pendu, proposition, a , l

#Début

print("\n\nBienvenu au Pendu, jeu consistant à trouver un mot en devinant\nquelles sont les lettres qui le composent.\nVous commencez avec 10 chances.")

print("\nSaisir un mot: " , end="")
motsecret = saisie_securisee()

enregistre_mot(motsecret, 0)

affiche_motsecret(pendu, 0)

while True :

    pendu, proposition, a, l = devinette(pendu, proposition, 1, l)

    print("Proposez une lettre: ", end='')
    proposition = input()

    if proposition in l:
        print('Vous avez déjà proposer "',proposition,'".')
    else:
        l.append(proposition)

    if proposition not in pendu and proposition in l:
            vie -= 1
            print("\nIl vous reste:",vie,"chances.")

    if a == len(pendu) :
        print("Bravo vous avez trouvé le bon mot !!!\n")
        print('Mot secret"',motsecret,'".\n')
        break
    elif vie == 0:
        print('Le mot secret était:"',motsecret,'".\nVous avez perdu.\n')
        break

print("Merci d'avoir jouer ! ")
