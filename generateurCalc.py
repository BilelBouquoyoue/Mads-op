from random import *

allChiffre = []
ordre = [0, 1, 2, 3]
operation = ['-', '+', '*', '/']
operationDivBug = ['-', '+', '*']
OperationUser = ['-', '+', '*']
ChiffreUser = [0, 1, 2, 3]

def genererLesChiffres():
    chiffre1 = randint(1, 10)
    chiffre2 = randint(1, 10)
    chiffre3 = randint(1, 10)
    chiffre4 = randint(1, 10)
    allChiffre.append(chiffre1)
    allChiffre.append(chiffre2)
    allChiffre.append(chiffre3)
    allChiffre.append(chiffre4)

def genererOrdre():
    shuffle(ordre)


def genererOperations():
    shuffle(operation)

def genererCalcul():
    genererLesChiffres()
    genererOperations()
    genererOrdre()
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
    tabAffichage = allChiffre
    shuffle(tabAffichage)
    print(f'Quel est le dévellopement pour trouver le résultat avec ces 4 chiffres ? (Chaque chiffre = 1 seule utilisation)')
    print(f'Les chiffres : {tabAffichage[0]}, {tabAffichage[1]}, {tabAffichage[2]}, {tabAffichage[3]}')
    print(f'Le résultat : {genererCalcul()}')
    print('Insert ton 1er chiffre')
    ChiffreUser[0] = input()
    while ChiffreUser[0].isdigit() == False:
        print('Insert ton 1er chiffre')
        ChiffreUser[0] = input()
    print('Insert ta 1ere opération')
    OperationUser[0] = input()
    print('Insert ton 2eme chiffre')
    ChiffreUser[1] = input()
    while ChiffreUser[1].isdigit() == False:
        print('Insert ton 1er chiffre')
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

genererCalcul()
affichageConsole()





