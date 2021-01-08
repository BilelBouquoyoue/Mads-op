from calcul import Calcul
from composants import Composants


# creer une classe pour la partie
class Game:
    """
    Classe permettant d'appeler les autres classes et de démarrer le jeu
    :type score = int
    :type vie = int
    :type vie_max = int
    """

    def __init__(self):
        """
        Initialisation du jeu
        """
        # jeu demarre
        self.score = 0
        self.vie = 3
        self.vie_max = 3
        self.en_jeu = True
        self.composants = Composants()

    def reussi(self):
        """
        En cas de réussite, le score de l'utilisateur augmente de 1
        :return: renvoie le nouveau score
        """
        self.score += 1

    def echec(self):
        """
        En cas d'echec du calcul, l'utilisateur perd une vie
        :return: renvoie le nouveau nombre de vie
        """
        self.vie = self.vie - 1

    def start(self):
        """
        Si l'utilisateur redémarre sa partie, le jeu est remis à zéro
        :return: le score de l'utilisateur est mis à 0
        :return: les vies de l'utilisateur sont à nouveau au maximum
        """
        self.score = 0
        self.vie = self.vie_max

    def game_over(self):
        """
        Si l'utilisateur ne redémarre pas la partie, le jeu s'arrète
        :return: null
        """
        self.composants.affichage_console('game_over')
        print(f'Mais bravo tout de même! Vous avez eu un score de {self.score}')

    def yes_no_question(self, question):
        """
        Ne permet à l'utilisateur de répondre que par yes ou no et aucun autre choix
        :param question: La  question posée à l'utilisateur
        :return: La réponse de l'utilisateur s'il répond par un des deux choix possible
        """
        yes_no_reponse = input(question).lower()
        if yes_no_reponse == "yes" or yes_no_reponse == "no":
            return yes_no_reponse
        else:
            print('Vous devez répondre par "yes" ou "no", pas autre chose')
            return self.yes_no_question(question)

    def jeu(self):
        """
        Démarre le jeu et appelle les différentes classes
        :return: null
        """
        nouveau_composant = Composants()
        nouveau_calcul = Calcul(nouveau_composant.chiffre_complet)
        nouveau_calcul.calcul_algorithme(nouveau_composant.chiffre_complet,
                                         nouveau_composant.operation, nouveau_composant.operation_div_erreur)
        nouveau_composant.composant_utilisateur(nouveau_calcul.resultat_algo)
        nouveau_calcul.calcul_utilisateur(nouveau_composant.chiffre_utilisateur,
                                          nouveau_composant.operation_utilisateur,
                                          nouveau_composant.operation_div_erreur)
        nouveau_calcul.verif_egalite(self)
