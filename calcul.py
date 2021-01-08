from random import *


class Calcul:
    """
    Classe permettant d'appeler les autres classes et de démarrer le jeu
    :type resultat_algo = int
    :type resultat_utilisateur = int
    """

    def __init__(self, tableau_chiffre):
        """
        Initialisation du calcul
        :param tableau_chiffre: Tableau contenant les chiffres du calcul
        """
        self.resultat_algo = tableau_chiffre[0]
        self.resultat_utilisateur = 0

        # Operation entre les 2 premiers chiffres

    def calcul_algorithme(self, tableau_chiffre, tableau_operation, tableau_operation_erreur):
        """
        Méthode permettant de faire le calcul du jeu
        :param tableau_chiffre: Tableau contenant les chiffres du calcul
        :param tableau_operation: Tableau contenant les opérations du calcul
        :param tableau_operation_erreur: Tableau contenant les 4 opérations
        """
        if tableau_operation and tableau_chiffre and tableau_operation_erreur:
            self.resultat_utilisateur = tableau_chiffre[0]
            if tableau_operation[0] == '/':
                if self.resultat_algo % tableau_chiffre[1] == 0:
                    self.resultat_algo = self.resultat_algo / tableau_chiffre[1]
                else:
                    nouvelle_operation = tableau_operation_erreur[randint(0, 2)]
                    if nouvelle_operation == '+':
                        self.resultat_algo = self.resultat_algo + tableau_chiffre[1]
                    elif nouvelle_operation == '-':
                        self.resultat_algo = self.resultat_algo - tableau_chiffre[1]
                    elif nouvelle_operation == '*':
                        self.resultat_algo = self.resultat_algo * tableau_chiffre[1]

            elif tableau_operation[0] == '+':
                self.resultat_algo = self.resultat_algo + tableau_chiffre[1]
            elif tableau_operation[0] == '-':
                self.resultat_algo = self.resultat_algo - tableau_chiffre[1]
            elif tableau_operation[0] == '*':
                self.resultat_algo = self.resultat_algo * tableau_chiffre[1]
            # operation avec le 3eme chiffre
            shuffle(tableau_operation)
            if tableau_operation[0] == '/':
                if self.resultat_algo % tableau_chiffre[2] == 0:
                    self.resultat_algo = self.resultat_algo / tableau_chiffre[2]
                else:
                    nouvelle_operation = tableau_operation_erreur[randint(0, 2)]
                    if nouvelle_operation == '+':
                        self.resultat_algo = self.resultat_algo + tableau_chiffre[2]
                    elif nouvelle_operation == '-':
                        self.resultat_algo = self.resultat_algo - tableau_chiffre[2]
                    elif nouvelle_operation == '*':
                        self.resultat_algo = self.resultat_algo * tableau_chiffre[2]

            elif tableau_operation[0] == '+':
                self.resultat_algo = self.resultat_algo + tableau_chiffre[2]
            elif tableau_operation[0] == '-':
                self.resultat_algo = self.resultat_algo - tableau_chiffre[2]
            elif tableau_operation[0] == '*':
                self.resultat_algo = self.resultat_algo * tableau_chiffre[2]

            # Operation avec le 4eme chiffre
            shuffle(tableau_operation)
            if tableau_operation[0] == '/':
                if self.resultat_algo % tableau_chiffre[3] == 0:
                    self.resultat_algo = self.resultat_algo / tableau_chiffre[3]
                else:
                    nouvelle_operation = tableau_operation_erreur[randint(0, 2)]
                    if nouvelle_operation == '+':
                        self.resultat_algo = self.resultat_algo + tableau_chiffre[3]
                    elif nouvelle_operation == '-':
                        self.resultat_algo = self.resultat_algo - tableau_chiffre[3]
                    elif nouvelle_operation == '*':
                        self.resultat_algo = self.resultat_algo * tableau_chiffre[3]

            elif tableau_operation[0] == '+':
                self.resultat_algo = self.resultat_algo + tableau_chiffre[3]
            elif tableau_operation[0] == '-':
                self.resultat_algo = self.resultat_algo - tableau_chiffre[3]
            elif tableau_operation[0] == '*':
                self.resultat_algo = self.resultat_algo * tableau_chiffre[3]

    @staticmethod
    def check_tableau_utilisateur(tableau):
        """
        Méthode vérifiant si la valeur entrée est une liste
        :param tableau: tableau de valeur
        :return:
        """
        if type(tableau) == list:
            return True
        else:
            return False

    @staticmethod
    def check_tableau_taille(tableau):
        """
        Méthode vérifiant si le tableau entrée est vide ou non
        :param tableau: de valeur
        :return:
        """
        if not tableau:
            return False
        else:
            return True

    def calcul_utilisateur(self, tableau_chiffre, tableau_operation, tableau_operation_erreur):
        """
        Méthode permettant de faire le calcul de l'utilisateur
        :param tableau_chiffre: tableau de valeur
        :param tableau_operation: tableau d'opération
        :param tableau_operation_erreur: tableau d'opération sans division
        :return:
        """
        tableau_chiffre[0] = int(tableau_chiffre[0])
        tableau_chiffre[1] = int(tableau_chiffre[1])
        tableau_chiffre[2] = int(tableau_chiffre[2])
        tableau_chiffre[3] = int(tableau_chiffre[3])
        self.resultat_utilisateur = tableau_chiffre[0]

        # Operation entre les 2 premiers chiffres
        if tableau_operation[0] == '/':
            if self.resultat_utilisateur % tableau_chiffre[1] == 0:
                self.resultat_utilisateur = self.resultat_utilisateur / tableau_chiffre[1]
            else:
                nouvelle_operation = tableau_operation_erreur[randint(0, 2)]
                if nouvelle_operation == '+':
                    self.resultat_utilisateur = self.resultat_utilisateur + tableau_chiffre[1]
                elif nouvelle_operation == '-':
                    self.resultat_utilisateur = self.resultat_utilisateur - tableau_chiffre[1]
                elif nouvelle_operation == '*':
                    self.resultat_utilisateur = self.resultat_utilisateur * tableau_chiffre[1]

        elif tableau_operation[0] == '+':
            self.resultat_utilisateur = self.resultat_utilisateur + tableau_chiffre[1]
        elif tableau_operation[0] == '-':
            self.resultat_utilisateur = self.resultat_utilisateur - tableau_chiffre[1]
        elif tableau_operation[0] == '*':
            self.resultat_utilisateur = self.resultat_utilisateur * tableau_chiffre[1]

        # operation avec le 3eme chiffre
        if tableau_operation[1] == '/':
            if self.resultat_utilisateur % tableau_chiffre[2] == 0:
                self.resultat_utilisateur = self.resultat_utilisateur / tableau_chiffre[2]
            else:
                nouvelle_operation = tableau_operation_erreur[randint(0, 2)]
                if nouvelle_operation == '+':
                    self.resultat_utilisateur = self.resultat_utilisateur + tableau_chiffre[2]
                elif nouvelle_operation == '-':
                    self.resultat_utilisateur = self.resultat_utilisateur - tableau_chiffre[2]
                elif nouvelle_operation == '*':
                    self.resultat_utilisateur = self.resultat_utilisateur * tableau_chiffre[2]

        elif tableau_operation[1] == '+':
            self.resultat_utilisateur = self.resultat_utilisateur + tableau_chiffre[2]
        elif tableau_operation[1] == '-':
            self.resultat_utilisateur = self.resultat_utilisateur - tableau_chiffre[2]
        elif tableau_operation[1] == '*':
            self.resultat_utilisateur = self.resultat_utilisateur * tableau_chiffre[2]

        # Operation avec le 4eme chiffre
        shuffle(tableau_operation)
        if tableau_operation[2] == '/':
            if self.resultat_utilisateur % tableau_chiffre[3] == 0:
                self.resultat_utilisateur = self.resultat_utilisateur / tableau_chiffre[3]
            else:
                nouvelle_operation = tableau_operation_erreur[randint(0, 2)]
                if nouvelle_operation == '+':
                    self.resultat_utilisateur = self.resultat_utilisateur + tableau_chiffre[3]
                elif nouvelle_operation == '-':
                    self.resultat_utilisateur = self.resultat_utilisateur - tableau_chiffre[3]
                elif nouvelle_operation == '*':
                    self.resultat_utilisateur = self.resultat_utilisateur * tableau_chiffre[3]

        elif tableau_operation[2] == '+':
            self.resultat_utilisateur = self.resultat_utilisateur + tableau_chiffre[3]
        elif tableau_operation[2] == '-':
            self.resultat_utilisateur = self.resultat_utilisateur - tableau_chiffre[3]
        elif tableau_operation[2] == '*':
            self.resultat_utilisateur = self.resultat_utilisateur * tableau_chiffre[3]

    def verif_egalite(self, partie):
        """
        Méthode permettant de comparer les réponses et dire à l'utilisateur s'il a eu raison ou tord
        :param partie: classe où doit s'effectuer la méthode
        :return: la réponse de l'utilisateur et celle attendue
        """
        if self.resultat_utilisateur == self.resultat_algo:
            print(f'Bravo! Vous avez trouvé la solution! Votre résultat est bien égal à {self.resultat_algo}.')
            partie.reussi()
            print(f'Vies restantes : {partie.vie}.\nVotre score : {partie.score}')
        else:
            print(
                f'Dommage! Vous avez mal répondu. Votre dévellopement à pour réponse {self.resultat_utilisateur} et'
                f' non {self.resultat_algo}.')
            partie.echec()
            print(f'Vies restantes : {partie.vie}.\nVotre score : {partie.score}')
