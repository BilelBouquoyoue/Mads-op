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
        self.calcul = Calcul(self.composants.chiffre_complet)

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

    def start(self, score=None, vie_max=None):
        """
        Si l'utilisateur redémarre sa partie, le jeu est remis à zéro
        :return: le score de l'utilisateur est mis à 0
        :return: les vies de l'utilisateur sont à nouveau au maximum
        """
        if score is None:
            self.score = 0
        else:
            self.score = score

        if vie_max is None:
            self.vie = self.vie_max
        else:
            self.vie = vie_max

    def game_over(self):
        """
        Si l'utilisateur ne redémarre pas la partie, le jeu s'arrète
        :return: null
        """
        self.composants.affichage_console('game_over')
        self.composants.affichage_console('bravo', self.score)

    def verif_egalite(self):
        """
        Méthode permettant de comparer les réponses et dire à l'utilisateur s'il a eu raison ou tord
        :return: la réponse de l'utilisateur et celle attendue
        """
        a = self.composants
        b = self.calcul
        a.value = self.calcul.resultat_utilisateur
        b.value = self.calcul.resultat_algo

        if a == b:
            a.affichage_console('reussi', self.calcul.resultat_algo)
            self.reussi()
            a.affichage_console('vie perdu', self.vie)
        else:
            a.affichage_console('echec', self.calcul.resultat_utilisateur, self.calcul.resultat_algo)
            self.echec()
            a.affichage_console('score_gagné', self.score)

    def oui_non_question(self, question, reponse=None):
        """
        Ne permet à l'utilisateur de répondre que par oui ou non et aucun autre choix
        :param reponse: permet de donner la réponse si déjà connu
        :param question: La  question posée à l'utilisateur
        :return: La réponse de l'utilisateur s'il répond par un des deux choix possible
        """
        if reponse is None:
            oui_non_reponse = input(question).lower()
            if oui_non_reponse == "oui" or oui_non_reponse == "non":
                return oui_non_reponse
            else:
                self.composants.affichage_console('oui ou non')
                return self.oui_non_question(question)
        else:
            return reponse.lower()

    def jeu(self):
        """
        Démarre le jeu et appelle les différentes classes
        :return: null
        """
        self.calcul.calcul_algorithme(self.composants.chiffre_complet,
                                      self.composants.operation, self.composants.operation_div_erreur)
        self.composants.composant_utilisateur(self.calcul.resultat_algo)
        self.calcul.calcul_utilisateur(self.composants.chiffre_utilisateur,
                                       self.composants.operation_utilisateur,
                                       self.composants.operation_div_erreur)
        self.verif_egalite()
