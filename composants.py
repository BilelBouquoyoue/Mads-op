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
        for i in range(4):
            self.chiffre_complet.append(randint(1, 10))
        self.operation = ['-', '+', '*', '/']
        self.operation_div_erreur = ['-', '+', '*']
        shuffle(self.operation)
        self.chiffre_utilisateur = [0, 1, 2, 3]
        self.operation_utilisateur = ['-', '+', '*']

    def __eq__(self, other):
        print("Composants __eq__ est appelé")
        return self.value == other

    @staticmethod
    def check_composant_utilisateur(resulta_algo):
        """
        Méthode permettant de regarder si le résultat est bien un int ou un float
        :param resulta_algo: le résultat attendu
        :return: True or False
        """
        return type(resulta_algo) == int or type(resulta_algo) == float

    def melanger(self, tableau):
        """
        Methode permettant de vérifier si un tableau est vide et le mélanger dans le cas contraire
        :param tableau: le tableau des valeurs à melanger
        :return:
        """
        if not tableau:
            self.affichage_console('tableau vide')
            return False
        else:
            shuffle(tableau)
            return tableau

    def affichage_console(self, a, b=None, c=None):
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

        elif a == 'affichage' and b:
            print(f'Le résultat attendue est {b}')
            return True

        elif a == 'chiffre affiché' and b:
            print(f'Les chiffres : {b}')
            return True

        elif a == 'tableau vide':
            print('Le tableau est vide')
            return True

        elif a == 'chiffre 4' and b:
            print(f'Ton 4eme chiffre utilisé est le {b}')
            return True

        elif a == 'pas dans la liste' and b:
            print(f"{b} n'est pas dans la liste")
            return True

        elif a == 'bravo' and b:
            print(f'Mais bravo tout de même! Vous avez eu un score de {b}')
            return True

        elif a == 'oui ou non':
            print('Vous devez répondre par "oui" ou "non", pas autre chose')
            return True

        elif a == 'démarrage':
            print('Le jeu redémarre')
            return True

        elif a == 'stop':
            print("Le jeu va s'arréter!\n"
                  "Bonne journée à vous.")
            return True

        elif a == 'echec' and b and c:
            print(
                f'Dommage! Vous avez mal répondu. Votre dévellopement à pour réponse {b} et'
                f' non {c}.')
            return True

        elif a == 'vie perdu' and b:
            print(f'Vous perdez une vie! Il vous reste {b} vies.')
            return True

        elif a == 'score gagné' and b:
            print(f'Votre score augmente de 1. Il est donc actuellement {b}')
            return True

        elif a == 'reussi' and b:
            print(f'Bravo! Vous avez trouvé la solution! Votre résultat est bien égal à {b}.')
            return True

        else:
            return False

    def choix_chiffre_operation(self, tableau, resultat, chiffre=None, operation=None):
        """
        Méthode permettant de choisir un chiffre et une opération, en cas d'erreur on redemande à l'utilisateur
        d'introduire les données
        :param operation: input demandant operation à l'utilisateur
        :param chiffre: input demandant un chiffre à l'utilisateur
        :param tableau: tableau des valeurs
        :param resultat: résultat attendu
        :return:
        """
        if tableau and resultat:
            self.affichage_console('affichage', resultat)
            length = len(tableau)
            chiffre_tableau = False
            for i in range(length):
                self.affichage_console('chiffre affiché', tableau[i])
            self.affichage_console('chiffre')
            if chiffre is None:
                chiffre = input()
            if int(chiffre) in tableau:
                chiffre_tableau = True
            self.melanger(tableau)

            if chiffre_tableau:
                self.affichage_console('operation')
                if operation is None:
                    operation = input()
                while not operation == '/' and not operation == '+' \
                        and not operation == '-' \
                        and not operation == '*':
                    self.affichage_console('erreur operation')
                    operation = input()
                tableau.remove(int(chiffre))
                return chiffre, operation
            else:
                self.affichage_console('erreur chiffre')
                self.affichage_console('pas dans la liste', chiffre)
                return self.choix_chiffre_operation(tableau, resultat)

    def composant_utilisateur(self, resultat, tableau=None):
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
            if tableau is None:
                for i in range(3):
                    a = self.choix_chiffre_operation(tableau_copie, resultat)
                    self.chiffre_utilisateur[i] = a[0]
                    self.operation_utilisateur[i] = a[1]
                self.affichage_console('chiffre 4', tableau_copie[0])
                self.chiffre_utilisateur[3] = tableau_copie[0]
            else:
                for i in range(3):
                    self.chiffre_utilisateur[i] = tableau[i]
