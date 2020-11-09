from random import *

allChiffre = []
operation = ['-', '+', '*', '/']
operationDivBug = ['-', '+', '*']
OperationUser = ['-', '+', '*']
ChiffreUser = [0, 1, 2, 3]
resultatAlgo = []
resultatUser = []
vie = [0]
score = [0]

def genererLesChiffres():
    chiffre1 = randint(1, 10)
    chiffre2 = randint(1, 10)
    chiffre3 = randint(1, 10)
    chiffre4 = randint(1, 10)
    allChiffre.append(chiffre1)
    allChiffre.append(chiffre2)
    allChiffre.append(chiffre3)
    allChiffre.append(chiffre4)

def genererOperations():
    shuffle(operation)


def calculerUser():
    if len(resultatUser) > 0:
        del resultatUser[0]
    ChiffreUser[0] = int(ChiffreUser[0])
    ChiffreUser[1] = int(ChiffreUser[1])
    ChiffreUser[2] = int(ChiffreUser[2])
    ChiffreUser[3] = int(ChiffreUser[3])
    print(ChiffreUser)

    resultat = ChiffreUser[0]

#Operation entre les 2 premiers chiffres
    if OperationUser[0] == '/':
        if resultat % ChiffreUser[1] == 0:
            resultat = resultat / ChiffreUser[1]
        else:
            newOp = operationDivBug[randint(0, 2)]
            if newOp == '+':
                resultat = resultat + ChiffreUser[1]
            elif newOp == '-':
                resultat = resultat - ChiffreUser[1]
            elif newOp == '*':
                resultat = resultat * ChiffreUser[1]

    elif OperationUser[0] == '+':
        resultat = resultat + ChiffreUser[1]
    elif OperationUser[0] == '-':
        resultat = resultat - ChiffreUser[1]
    elif OperationUser[0] == '*':
        resultat = resultat * ChiffreUser[1]
    #operation avec le 3eme chiffre
    if OperationUser[1] == '/':
        if resultat % ChiffreUser[2] == 0:
            resultat = resultat / ChiffreUser[2]
        else:
            newOp = operationDivBug[randint(0, 2)]
            if newOp == '+':
                resultat = resultat + ChiffreUser[2]
            elif newOp == '-':
                resultat = resultat - ChiffreUser[2]
            elif newOp == '*':
                resultat = resultat * ChiffreUser[2]

    elif OperationUser[1] == '+':
        resultat = resultat + ChiffreUser[2]
    elif OperationUser[1] == '-':
        resultat = resultat - ChiffreUser[2]
    elif OperationUser[1] == '*':
        resultat = resultat * ChiffreUser[2]

    #Operation avec le 4eme chiffre
    shuffle(operation)
    if OperationUser[2] == '/':
        if resultat % ChiffreUser[3] == 0:
            resultat = resultat / ChiffreUser[3]
        else:
            newOp = operationDivBug[randint(0, 2)]
            if newOp == '+':
                resultat = resultat + ChiffreUser[3]
            elif newOp == '-':
                resultat = resultat - ChiffreUser[3]
            elif newOp == '*':
                resultat = resultat * ChiffreUser[3]

    elif OperationUser[2] == '+':
        resultat = resultat + ChiffreUser[3]
    elif OperationUser[2] == '-':
        resultat = resultat - ChiffreUser[3]
    elif OperationUser[2] == '*':
        resultat = resultat * ChiffreUser[3]
    resultatUser.append(resultat)
    return resultat



def genererCalcul():

    resultat = allChiffre[0]

    #Operation entre les 2 premiers chiffres
    if operation[0] == '/':
        if resultat % allChiffre[1] == 0:
            resultat = resultat / allChiffre[1]
        else:
            newOp = operationDivBug[randint(0, 2)]
            if newOp == '+':
                resultat = resultat + allChiffre[1]
            elif newOp == '-':
                resultat = resultat - allChiffre[1]
            elif newOp == '*':
                resultat = resultat * allChiffre[1]

    elif operation[0] == '+':
        resultat = resultat + allChiffre[1]
    elif operation[0] == '-':
        resultat = resultat - allChiffre[1]
    elif operation[0] == '*':
        resultat = resultat * allChiffre[1]
    #operation avec le 3eme chiffre
    shuffle(operation)
    if operation[0] == '/':
        if resultat % allChiffre[2] == 0:
            resultat = resultat / allChiffre[2]
        else:
            newOp = operationDivBug[randint(0, 2)]
            if newOp == '+':
                resultat = resultat + allChiffre[2]
            elif newOp == '-':
                resultat = resultat - allChiffre[2]
            elif newOp == '*':
                resultat = resultat * allChiffre[2]

    elif operation[0] == '+':
        resultat = resultat + allChiffre[2]
    elif operation[0] == '-':
        resultat = resultat - allChiffre[2]
    elif operation[0] == '*':
        resultat = resultat * allChiffre[2]

    #Operation avec le 4eme chiffre
    shuffle(operation)
    if operation[0] == '/':
        if resultat % allChiffre[3] == 0:
            resultat = resultat / allChiffre[3]
        else:
            newOp = operationDivBug[randint(0, 2)]
            if newOp == '+':
                resultat = resultat + allChiffre[3]
            elif newOp == '-':
                resultat = resultat - allChiffre[3]
            elif newOp == '*':
                resultat = resultat * allChiffre[3]

    elif operation[0] == '+':
        resultat = resultat + allChiffre[3]
    elif operation[0] == '-':
        resultat = resultat - allChiffre[3]
    elif operation[0] == '*':
        resultat = resultat * allChiffre[3]
    return resultat




def affichageConsole():
    if len(resultatAlgo) > 0:
        del resultatAlgo[0]
    resultatAlgo.append(genererCalcul())
    tabAffichage = allChiffre
    shuffle(tabAffichage)
    print(f'Quel est le dévellopement pour trouver le résultat avec ces 4 chiffres ? (Chaque chiffre = 1 seule utilisation)')
    print(f'Les chiffres : {tabAffichage[0]}, {tabAffichage[1]}, {tabAffichage[2]}, {tabAffichage[3]}')
    print(f'Le résultat : {resultatAlgo[0]}')
    print('Insert ton 1er chiffre')
    ChiffreUser[0] = input()
    while ChiffreUser[0].isdigit() == False:
        print('Insert ton 1er chiffre. Et pas autre chose!')
        ChiffreUser[0] = input()
    print('Insert ta 1ere opération')
    OperationUser[0] = input()
    """while OperationUser[0] != '/' or OperationUser[0] != '+' or OperationUser[0] != '-' or OperationUser[0] != '*':
        print('Insert ta 1ere opération')
        OperationUser[0] = input()"""
    print('Insert ton 2eme chiffre')
    ChiffreUser[1] = input()
    while ChiffreUser[1].isdigit() == False:
        print('Insert ton 2eme chiffre (et pas des lettres!)')
        ChiffreUser[1] = input()
    print('Insert ta 2eme opération')
    OperationUser[1] = input()
    print('Insert ton 3eme chiffre')
    ChiffreUser[2] = input()
    while ChiffreUser[2].isdigit() == False:
        print('Insert ton 1er chiffre')
        ChiffreUser[2] = input()
    print('Insert ta 3eme opération')
    OperationUser[2] = input()
    print('Insert ton 4eme chiffre')
    ChiffreUser[3] = input()
    while ChiffreUser[3].isdigit() == False:
        print('Insert ton 1er chiffre')
        ChiffreUser[3] = input()
    print(ChiffreUser)
    print(OperationUser)

def verifEgalité():
    scoreU = score[0]
    vieU = vie[0]
    if resultatAlgo[0] == resultatUser[0]:
        print(f'Bravo! Vous avez trouvé la solution! Votre résultat est bien égal à {resultatAlgo[0]}.')
        scoreU += 1
        score[0] = scoreU
        print(f'Vies restantes : {vie[0]}')
        print(f'Votre score : {score[0]}')
    else:
        print(f'Dommage! Vous avez mal répondu. Votre dévellopement à pour réponse {resultatUser[0]} et non {resultatAlgo[0]}.')
        vieU -= 1
        vie[0] = vieU
        print(f'Vies restantes : {vie[0]}')
        print(f'Votre score : {score[0]}')



def calculComplet():
    vie[0] = 3
    while vie[0] > 0:
        print('----------------------------------------------------------------------------------------------------------------------')
        genererLesChiffres()
        genererOperations()
        affichageConsole()
        calculerUser()
        verifEgalité()
    print(f'Vous avez perdu! Il ne vous reste plus de vie. Votre score est de : {score[0]}')


calculComplet()






