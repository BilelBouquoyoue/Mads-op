from random import *


class Calcul:
    """
    Classe permettant d'appeler les autres classes et de démarrer le jeu
    :type resultatA = int
    :type resultatU = int
    """

    def __init__(self, tableau_chiffre):
        """
        Initialisation du calcul
        :param tableau_chiffre: Tableau contenant les chiffres du calcul
        """
        self.resultatA = tableau_chiffre[0]
        self.resultatU = 0

        # Operation entre les 2 premiers chiffres

    def calculerAlgo(self, tabC, tabO, tabOB):
        """
        Méthode permettant de faire les différents calculs
        :param tabC: Tableau contenant les chiffres du calcul
        :param tabO: Tableau contenant les opérations du calcul
        :param tabOB: Tableau contenant les 4 opérations
        """
        if tabO and tabC and tabOB:
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
            shuffle(tabO)
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

    @staticmethod
    def check_tableau_user(tableau):
        if type(tableau) == list:
            return True
        else:
            return False

    @staticmethod
    def check_tableau_taille(tableau):
        if not tableau:
            return False
        else:
            return True

    def calculerUser(self, tabC, tabO, tabOB):

        tabC[0] = int(tabC[0])
        tabC[1] = int(tabC[1])
        tabC[2] = int(tabC[2])
        tabC[3] = int(tabC[3])
        self.resultatU = tabC[0]
        balise2 = self.check_tableau_taille(self.resultatU)
        if balise2:
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
            shuffle(tabO)
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
        else:
            False

    def verifEgalite(self, partie):
        """
        Méthode permettant de comparer les réponses et dire à l'utilisateur s'il a eu raison ou tord
        :param partie: classe où doit s'effectuer la méthode
        :return: la réponse de l'utilisateur et celle attendue
        """
        if self.resultatU == self.resultatA:
            print(f'Bravo! Vous avez trouvé la solution! Votre résultat est bien égal à {self.resultatA}.')
            partie.reussi()
            print(f'Vies restantes : {partie.vie}.\nVotre score : {partie.score}')
        else:
            print(
                f'Dommage! Vous avez mal répondu. Votre dévellopement à pour réponse {self.resultatU} et'
                f' non {self.resultatA}.')
            partie.echec()
            print(f'Vies restantes : {partie.vie}.\nVotre score : {partie.score}')

