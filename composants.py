from random import *


class Composants:
    """
    Classe créeant tout les composants du calcul
    :type chiffre_complet: list
    :type operation: list
    :type operation_div_erreur: list
    :type operation_utilisateur: list
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
        self.operation_div_erreur = ['-', '+', '*']
        shuffle(self.operation)
        self.chiffre_utilisateur = [0, 1, 2, 3]
        self.operation_utilisateur = ['-', '+', '*']

    @staticmethod
    def check_composant_utilisateur(resulta_algo):
        """
        Méthode permettant de regarder si le résultat est bien un int ou un float
        :param resulta_algo: le résultat attendu
        :return: True or False
        """
        if type(resulta_algo) == int:
            return True
        elif type(resulta_algo) == float:
            return True
        else:
            return False

    @staticmethod
    def melanger(tableau):
        """
        Methode permettant de vérifier si un tableau est vide et le mélanger dans le cas contraire
        :param tableau: le tableau des valeurs à melanger
        :return:
        """
        if not tableau:
            print('Le tableau est vide')
            return False
        else:
            shuffle(tableau)
            return tableau

    def affichage_console(self, a):
        """
        Méthode permettant d'afficher en console des phrases préintroduite
        :param a: string permttant le choix du message en console
        :return:
        """
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
        """
        Méthode permettant de choisir un chiffre et une opération, en cas d'erreur on redemande à l'utilisateur
        d'introduire les données
        :param tableau: tableau des valeurs
        :param resultat: résultat attendu
        :return:
        """
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
                self.affichage_console('erreur chiffre')
                print(chiffre, "n'est pas dans la liste")
                return self.choix_chiffre_operation(tableau, resultat)

    def composant_utilisateur(self, resultat):
        """
        Création du calcul de l'utilisateur en faisant attention à ce que seul les chiffres et opérations du caluls
        ne soit introduit
        :param resultat: Le résultat attendu
        :return:
        """
        balise = self.check_composant_utilisateur(resultat)
        if balise:
            tableau_affichage = self.chiffre_complet
            tableau_copie = tableau_affichage[:]
            self.melanger(tableau_affichage)
            self.affichage_console('regle')
            for i in range(3):
                self.choix_chiffre_operation(tableau_copie, resultat)

            print(f'Ton 4eme chiffre utilisé est le {tableau_copie[0]}')
            self.chiffre_utilisateur[3] = tableau_copie[0]
