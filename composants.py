from random import *


class Composants:
    """
    Classe créeant tout les composants du calcul
    :type chiffre_complet: list
    :type operation: list
    :type operationDivBug: list
    :type operationUser: list
    """

    def __init__(self):
        """
        Initialisation des listes du calcul et en les méleangeant
        """
        self.chiffre_complet = []
        self.chiffre_complet.append(randint(1, 10))
        self.chiffre_complet.append(randint(1, 10))
        self.chiffre_complet.append(randint(1, 10))
        self.chiffre_complet.append(randint(1, 10))
        self.operation = ['-', '+', '*', '/']
        self.operationDivBug = ['-', '+', '*']
        shuffle(self.operation)
        self.chiffreUser = [0, 1, 2, 3]
        self.operationUser = ['-', '+', '*']
        self.error = False

    @staticmethod
    def checkComposantUtilisateur(result_a):
        if type(result_a) == int:
            return True
        elif type(result_a) == float:
            return True
        else:
            return False

    @staticmethod
    def melanger(tableau):
        if not tableau:
            print('Le tableau est vide')
            return False
        else:
            shuffle(tableau)
            return tableau

    def affichage_console(self, a):
        if a == 'regle':
            print(
                f'Quel est le dévellopement pour trouver le résultat avec ces 4 chiffres ?'
                f' (Chaque chiffre = 1 seule utilisation)')
            return True

        elif a == "chiffre":
            print('Insert ton  chiffre')
            return True

        elif a == 'erreur chiffre':
            print("Vous n'avez pas entrez un bon chiffre, veuillez réessayer!")
            return True

        elif a == 'operation':
            print('Insert ton opération')
            return True

        elif a == 'erreur operation':
            print('Insert ton opération et pas autre chose')
            return True

        elif a == 'erreur logiciel':
            print('Une erreur est survenue. Veuillez relancer le jeu')
            return True

        elif a == 'game_over':
            print('Dommage! Vous ne possédez plus aucune vie. ')
            return True

        else:
            return False

    def choix_chiffre_operation(self, tableau, resultat):
        if tableau and resultat:
            print(f'Le résultat attendue est {resultat}')
            length = len(tableau)
            chiffre_tableau = False
            for i in range(length):
                print(f'Les chiffres : {tableau[i]}')
            self.affichage_console('chiffre')
            chiffre = input()
            if int(chiffre) in tableau:
                chiffre_tableau = True
            self.melanger(tableau)

            if chiffre_tableau:
                self.affichage_console('operation')
                operation = input()
                while not operation == '/' and not operation == '+' \
                        and not operation == '-' \
                        and not operation == '*':
                    self.affichage_console('erreur operation')
                    operation = input()
                tableau.remove(int(chiffre))
                return chiffre and operation
            else:
                print(chiffre, "n'est pas dans la liste")
                self.affichage_console('erreur chiffre')
                return self.choix_chiffre_operation(tableau, resultat)

    def composantUtilisateur(self, result_a):
        """
        Création du calcul de l'utilisateur en faisant attention à ce que seul les chiffres et opérations du caluls
        ne soit introduit
        :param result_a: Le résultat attendu
        :return:
        """
        balise = self.checkComposantUtilisateur(result_a)
        if balise:
            tabAffichage = self.chiffre_complet
            tabCopy = tabAffichage[:]
            self.melanger(tabAffichage)
            self.affichage_console('regle')
            for i in range(3):
                self.choix_chiffre_operation(tabCopy, result_a)

            print(f'Ton 4eme chiffre utilisé est le {tabCopy[0]}')
            self.chiffreUser[3] = tabCopy[0]
