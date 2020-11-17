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


class Partie:

    def __init__(self):
        self.score = 0
        self.vie = 3

    def reussi(self):
        self.score += 1

    def echec(self):
        self.vie = self.vie - 1



class Comparateur:
    """
    Classe d'un calcul
    """
    def __init__(self, resultatAlgo, resultatUser):
        self.resultatA = resultatAlgo
        self.resultatU = resultatUser

    def verifEgalité(self, partie):
        if self.resultatU == self.resultatA:
            print(f'Bravo! Vous avez trouvé la solution! Votre résultat est bien égal à {self.resultatA}.')
            partie.reussi()
            print(f'Vies restantes : {partie.vie}')
            print(f'Votre score : {partie.score}')
        else:
            print(f'Dommage! Vous avez mal répondu. Votre dévellopement à pour réponse {self.resultatU} et non {self.resultatA}.')
            partie.echec()
            print(f'Vies restantes : {partie.vie}')
            print(f'Votre score : {partie.score}')



class Composants:

    def __init__(self):
        self.allChiffre = []
        self.allChiffre.append(randint(1, 10))
        self.allChiffre.append(randint(1, 10))
        self.allChiffre.append(randint(1, 10))
        self.allChiffre.append(randint(1, 10))
        self.operation = ['-', '+', '*', '/']
        self.operationDivBug = ['-', '+', '*']
        shuffle(self.operation)
        self.chiffreUser = [0, 1, 2, 3]
        self.operationUser = ['-', '+', '*']

    def composantUtilisateur(self, resultA):
        tabAffichage = self.allChiffre
        tabCopy = tabAffichage[:]
        shuffle(tabAffichage)
        print(
            f'Quel est le dévellopement pour trouver le résultat avec ces 4 chiffres ? (Chaque chiffre = 1 seule utilisation)')
        print(f'Les chiffres : {tabAffichage[0]}, {tabAffichage[1]}, {tabAffichage[2]}, {tabAffichage[3]}')
        print(f'Le résultat : {resultA}')
        print('Insert ton 1er chiffre')
        self.chiffreUser[0] = input()
        while not self.chiffreUser[0] == str(tabAffichage[0]) and not self.chiffreUser[0] == str(tabAffichage[1]) \
                and not self.chiffreUser[0] == str(tabAffichage[2]) and not self.chiffreUser[0] == str(tabAffichage[3]):
            print('Insert ton 1er chiffre. Et pas autre chose!')
            self.chiffreUser[0] = input()

        try:
            tabCopy.remove(int(self.chiffreUser[0]))
        except ValueError:  # If ChiffreUser[0] is not in tabCopy
            print(self.chiffreUser[0], "is not in the list of number")
            print(tabCopy)

        shuffle(tabCopy)
        print('Insert ta 1ere opération')
        self.operationUser[0] = input()
        while not self.operationUser[0] == '/' and not self.operationUser[0] == '+' and not self.operationUser[0] == '-' and not \
                self.operationUser[0] == '*':
            print('Insert ta 1ère opération')
            self.operationUser[0] = input()

        print(f'Les chiffres restants: {tabCopy[0]}, {tabCopy[1]}, {tabCopy[2]}')
        print('Insert ton 2eme chiffre')
        self.chiffreUser[1] = input()
        while not self.chiffreUser[1] == str(tabCopy[0]) and not self.chiffreUser[1] == str(tabCopy[1]) and not self.chiffreUser[1] == str(tabCopy[2]):

            print('Insert ton 2eme chiffre (et pas des lettres!)')
            self.chiffreUser[1] = input()

        try:
            tabCopy.remove(int(self.chiffreUser[1]))
        except ValueError:  # If ChiffreUser[0] is not in tabCopy
            print(self.chiffreUser[1], "is not in the list of number")
            print(tabCopy)

        shuffle(tabCopy)
        print('Insert ta 2eme opération')
        self.operationUser[1] = input()
        while not self.operationUser[1] == '/' and not self.operationUser[1] == '+' and not self.operationUser[1] == '-' and not \
                self.operationUser[1] == '*':
            print('Insert ta 2ème opération')
            self.operationUser[1] = input()

        print(f'Les chiffres restants: {tabCopy[0]}, {tabCopy[1]}')
        print('Insert ton 3eme chiffre')
        self.chiffreUser[2] = input()
        while not self.chiffreUser[2] == str(tabCopy[0]) and not self.chiffreUser[2] == str(tabCopy[1]):
            print('Insert ton chiffre')
            self.chiffreUser[2] = input()

        try:
            tabCopy.remove(int(self.chiffreUser[2]))
        except ValueError:  # If ChiffreUser[0] is not in tabCopy
            print(self.chiffreUser[2], "is not in the list of number")
            print(tabCopy)

        shuffle(tabCopy)
        print('Insert ta 3eme opération')
        self.operationUser[2] = input()
        while not self.operationUser[2] == '/' and not self.operationUser[2] == '+' and not self.operationUser[2] == '-' and not \
                self.operationUser[2] == '*':
            print('Insert ta 3ème opération')
            self.operationUser[2] = input()

        print(f'Ton 4eme chiffre utilisé est le {tabCopy[0]}')
        self.chiffreUser[3] = tabCopy[0]
        print(self.chiffreUser)
        print(self.operationUser)


class Calculateur:

    def __init__(self, tabC):
        self.resultatA = tabC[0]

        # Operation entre les 2 premiers chiffres
    def calculerAlgo(self, tabC, tabO, tabOB):
        self.resultatU = tabC[0]
        if tabO[0] == '/':
            if self.resultatA % tabC[1] == 0:
                self.resultatA = self.resultatA / tabC[1]
            else:
                newOp = tabOB[randint(0, 2)]
                if newOp == '+':
                    self.resultatA = self.resultatA + tabC[1]
                elif newOp == '-':
                    self.resultatA = self.resultatA - tabC[1]
                elif newOp == '*':
                    self.resultatA = self.resultatA * tabC[1]

        elif tabO[0] == '+':
            self.resultatA = self.resultatA + tabC[1]
        elif tabO[0] == '-':
            self.resultatA = self.resultatA - tabC[1]
        elif tabO[0] == '*':
            self.resultatA = self.resultatA * tabC[1]
        # operation avec le 3eme chiffre
        shuffle(tabO)
        if tabO[0] == '/':
            if self.resultatA % tabC[2] == 0:
                self.resultatA = self.resultatA / tabC[2]
            else:
                newOp = tabOB[randint(0, 2)]
                if newOp == '+':
                    self.resultatA = self.resultatA + tabC[2]
                elif newOp == '-':
                    self.resultatA = self.resultatA - tabC[2]
                elif newOp == '*':
                    self.resultatA = self.resultatA * tabC[2]

        elif tabO[0] == '+':
            self.resultatA = self.resultatA + tabC[2]
        elif tabO[0] == '-':
            self.resultatA = self.resultatA - tabC[2]
        elif tabO[0] == '*':
            self.resultatA = self.resultatA * tabC[2]

        # Operation avec le 4eme chiffre
        shuffle(operation)
        if tabO[0] == '/':
            if self.resultatA % tabC[3] == 0:
                self.resultatA = self.resultatA / tabC[3]
            else:
                newOp = tabOB[randint(0, 2)]
                if newOp == '+':
                    self.resultatA = self.resultatA + tabC[3]
                elif newOp == '-':
                    self.resultatA = self.resultatA - tabC[3]
                elif newOp == '*':
                    self.resultatA = self.resultatA * tabC[3]

        elif tabO[0] == '+':
            self.resultatA = self.resultatA + tabC[3]
        elif tabO[0] == '-':
            self.resultatA = self.resultatA - tabC[3]
        elif tabO[0] == '*':
            self.resultatA = self.resultatA * tabC[3]

    def calculerUser(self, tabC, tabO, tabOB):
        tabC[0] = int(tabC[0])
        tabC[1] = int(tabC[1])
        tabC[2] = int(tabC[2])
        tabC[3] = int(tabC[3])
        print(tabC)

        self.resultatU = tabC[0]

        # Operation entre les 2 premiers chiffres
        if tabO[0] == '/':
            if self.resultatU % tabC[1] == 0:
                self.resultatU = self.resultatU / tabC[1]
            else:
                newOp = tabOB[randint(0, 2)]
                if newOp == '+':
                    self.resultatU = self.resultatU + tabC[1]
                elif newOp == '-':
                    self.resultatU = self.resultatU - tabC[1]
                elif newOp == '*':
                    self.resultatU = self.resultatU * tabC[1]

        elif tabO[0] == '+':
            self.resultatU = self.resultatU + tabC[1]
        elif tabO[0] == '-':
            self.resultatU = self.resultatU - tabC[1]
        elif tabO[0] == '*':
            self.resultatU = self.resultatU * tabC[1]
        # operation avec le 3eme chiffre
        if tabO[1] == '/':
            if self.resultatU % tabC[2] == 0:
                self.resultatU = self.resultatU / tabC[2]
            else:
                newOp = tabOB[randint(0, 2)]
                if newOp == '+':
                    self.resultatU = self.resultatU + tabC[2]
                elif newOp == '-':
                    self.resultatU = self.resultatU - tabC[2]
                elif newOp == '*':
                    self.resultatU = self.resultatU * tabC[2]

        elif tabO[1] == '+':
            self.resultatU = self.resultatU + tabC[2]
        elif tabO[1] == '-':
            self.resultatU = self.resultatU - tabC[2]
        elif tabO[1] == '*':
            self.resultatU = self.resultatU * tabC[2]

        # Operation avec le 4eme chiffre
        shuffle(operation)
        if tabO[2] == '/':
            if self.resultatU % tabC[3] == 0:
                self.resultatU = self.resultatU / tabC[3]
            else:
                newOp = tabOB[randint(0, 2)]
                if newOp == '+':
                    self.resultatU = self.resultatU + tabC[3]
                elif newOp == '-':
                    self.resultatU = self.resultatU - tabC[3]
                elif newOp == '*':
                    self.resultatU = self.resultatU * tabC[3]

        elif tabO[2] == '+':
            self.resultatU = self.resultatU + tabC[3]
        elif tabO[2] == '-':
            self.resultatU = self.resultatU - tabC[3]
        elif tabO[2] == '*':
            self.resultatU = self.resultatU * tabC[3]
        resultatUser.append(self.resultatU)
        print(self.resultatU)
        print(self.resultatA)

def calculComplet():
    newGame = Partie()
    while newGame.vie > 0:
        nouvComp = Composants()
        nouvCalc = Calculateur(nouvComp.allChiffre)
        nouvCalc.calculerAlgo(nouvComp.allChiffre, nouvComp.operation, nouvComp.operationDivBug)
        nouvComp.composantUtilisateur(nouvCalc.resultatA)
        nouvCalc.calculerUser(nouvComp.chiffreUser, nouvComp.operationUser, nouvComp.operationDivBug)
        nouvComparateur = Comparateur(nouvCalc.resultatA, nouvCalc.resultatU)
        nouvComparateur.verifEgalité(newGame)
    print(f'Dommage! Vous ne possédez plus aucune vie. Mais bravo tout de même! Vous avez eu un score de {newGame.score}')


calculComplet()



