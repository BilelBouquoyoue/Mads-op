from random import *


class Operation:

    def __init__(self, difficulte):
        self.difficulte = difficulte
        self.tabOperation = ['+', '-', '*', '/']
        self.bugDiv = False
        self.operationUser = ['-', '+', '*']

    def operation(self):
        d = self.difficulte

        if d == "Facile":
            print('Insert ta 1ere opération')
            self.operationUser[0] = input()
            while not self.operationUser[0] == '-' and not self.operationUser[0] == '+':
                print('Insert une soustraction ou une addition')
                self.operationUser[0] = input()

            print('Insert ta seconde opération')
            self.operationUser[1] = input()
            while not self.operationUser[1] == '-' and not self.operationUser[1] == '+':
                print('Insert une soustraction ou une addition')
                self.operationUser[1] = input()

            print('Insert ta dernière opération')
            self.operationUser[2] = input()
            while not self.operationUser[2] == '-' and not self.operationUser[2] == '+':
                print('Insert une soustraction ou une addition')
                self.operationUser[2] = input()

        elif d == 'Moyen':
            print('Insert ta 1ere opération')
            self.operationUser[0] = input()
            while not self.operationUser[0] == '-' and not self.operationUser[0] == '+' and not self.operationUser[
                                                                                                    0] == '*':
                print('Insert une soustraction ou une addition ou une multiplication')
                self.operationUser[0] = input()

            print('Insert ta seconde opération')
            self.operationUser[1] = input()
            while not self.operationUser[1] == '-' and not self.operationUser[1] == '+' and not self.operationUser[
                                                                                                    1] == '*':
                print('Insert une soustraction ou une addition ou une multiplication')
                self.operationUser[1] = input()

            print('Insert ta dernière opération')
            self.operationUser[2] = input()
            while not self.operationUser[2] == '-' and not self.operationUser[1] == '+' and not self.operationUser[
                                                                                                    2] == '*':
                print('Insert une soustraction ou une addition ou une multiplication')
                self.operationUser[2] = input()

        elif d == 'Difficile':
            print('Insert ta 1ere opération')
            self.operationUser[0] = input()
            while not self.operationUser[0] == '-' and not self.operationUser[0] == '+' and not self.operationUser[
                                                                                                    0] == '*' and not \
                    self.operationUser[0] == '/':
                print('Insert une soustraction ou une addition ou une multiplication')
                self.operationUser[0] = input()

            while self.operationUser[0] == '/':
                self.testBug(chiffreA, chiffreB)

            print('Insert ta seconde opération')
            self.operationUser[1] = input()
            while not self.operationUser[1] == '-' and not self.operationUser[1] == '+' and not self.operationUser[
                                                                                                    1] == '*' and not \
                    self.operationUser[1] == '/':
                print('Insert une soustraction ou une addition ou une multiplication')
                self.operationUser[1] = input()

            while self.operationUser[0] == '/':
                self.testBug(chiffreA, chiffreB)

            print('Insert ta dernière opération')
            self.operationUser[2] = input()
            while not self.operationUser[2] == '-' and not self.operationUser[1] == '+' and not self.operationUser[
                                                                                                    2] == '*' and not \
                    self.operationUser[2] == '/':
                print('Insert une soustraction ou une addition ou une multiplication')
                self.operationUser[2] = input()

            while self.operationUser[0] == '/':
                self.testBug(chiffreA, chiffreB)

    def testBug(self, chiffreA, chiffreB):
        if chiffreA % chiffreB[1] != 0:
            self.bugDiv = True
            self.resolutionBug(chiffreA, chiffreB)

    def resolutionBug(self, chiffreA, chiffreB):
        copie = 0
        if chiffreB % chiffreA[1] == 0:
            copie = chiffreA
            chiffreA = chiffreB
            chiffreB = chiffreA
            self.bugDiv = False

        else:
            newOp = self.tabOperation[randint(0, 2)]
