import unittest
from composants import Composants
from game import Game
from calcul import Calcul


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.composants = Composants()
        self.game = Game()
        self.answer_oui_capital = 'OUI'
        self.answer_non = 'non'
        self.tableau_plein = [1, 2, 3, 4]
        self.tableau_un = [1, 1, 1]
        self.tableau_vide = []
        self.resultat = 3
        self.chiffre_un = 1
        self.string_plus = '+'
        self.calcul = Calcul(self.tableau_plein)
        self.tabC = self.composants.chiffre_complet
        self.tabO = ['+', '/', '*', '-']
        self.tabOB = ['+', '*', '-']
        self.tab_plus = ['+']
        self.tab_moins = ['-']
        self.tab_div = ['/']
        self.tab_fois = ['*']

    def test_game(self):
        self.assertEqual(self.game.oui_non_question('Ecrire oui', self.answer_oui_capital), 'oui')
        self.assertEqual(self.game.oui_non_question('Ecrire ce que vous voulez', self.answer_non), 'non')
        self.assertTrue(self.game.en_jeu)
        self.assertEqual(self.game.score, 0)
        self.assertTrue(self.game.jeu)

    def test_check_composant(self):
        self.assertFalse(self.composants.check_composant_utilisateur('ezqdfza'))
        self.assertTrue(self.composants.check_composant_utilisateur(1))
        self.assertTrue(self.composants.check_composant_utilisateur(1.5))
        self.assertFalse(self.composants.check_composant_utilisateur(''))

    def test_check_tableau_user(self):
        self.assertTrue(self.calcul.check_tableau_utilisateur(self.tableau_plein))
        self.assertFalse(self.calcul.check_tableau_utilisateur(self.answer_non))
        self.assertTrue(self.calcul.check_tableau_taille(self.tableau_plein))
        self.assertFalse(self.calcul.check_tableau_taille(self.tableau_vide))

    def test_verif_egalite(self):
        self.assertIsNone(self.game.verif_egalite())

    def test_affichage_console(self):
        self.assertTrue(self.composants.affichage_console('regle'))
        self.assertTrue(self.composants.affichage_console('chiffre'))
        self.assertTrue(self.composants.affichage_console('erreur chiffre'))
        self.assertTrue(self.composants.affichage_console('operation'))
        self.assertTrue(self.composants.affichage_console('erreur operation'))
        self.assertTrue(self.composants.affichage_console('erreur logiciel'))
        self.assertTrue(self.composants.affichage_console('game_over'))
        self.assertTrue(self.composants.affichage_console('affichage', self.resultat))
        self.assertTrue(self.composants.affichage_console('affichage', self.tableau_plein))
        self.assertTrue(self.composants.affichage_console('tableau vide'))
        self.assertTrue(self.composants.affichage_console('chiffre 4', self.chiffre_un))
        self.assertTrue(self.composants.affichage_console('pas dans la liste', self.string_plus))
        self.assertTrue(self.composants.affichage_console('bravo', self.resultat))
        self.assertTrue(self.composants.affichage_console('oui ou non'))
        self.assertTrue(self.composants.affichage_console('démarrage'))
        self.assertTrue(self.composants.affichage_console('stop'))
        self.assertTrue(self.composants.affichage_console('echec', self.chiffre_un, self.resultat))
        self.assertTrue(self.composants.affichage_console('vie perdu', self.chiffre_un))
        self.assertTrue(self.composants.affichage_console('score gagné', self.chiffre_un))
        self.assertTrue(self.composants.affichage_console('reussi', self.resultat))
        self.assertFalse(self.composants.affichage_console('eza'))

    def test_choix_chiffre_operation(self):
        self.assertTrue(self.composants.choix_chiffre_operation(self.tableau_un, self.resultat,
                                                                self.chiffre_un, self.string_plus))

    def test_calculer_algo(self):
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tabO, self.tabOB))
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tab_plus, self.tabOB), '+')
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tab_moins, self.tabOB), '-')
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tab_fois, self.tabOB), '*')
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tab_div, self.tabOB), '+')
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tab_div, self.tabOB), '-')
        self.assertIsNone(self.calcul.calcul_algorithme(self.tabC, self.tab_div, self.tabOB), '*')

    def test_calculer_user(self):
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB))
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB), '+')
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB), '-')
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB), '*')
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB), '+')
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB), '-')
        self.assertIsNone(self.calcul.calcul_utilisateur(self.tabC, self.tabO, self.tabOB), '*')

    def test_composant_utilisateur(self):
        self.assertIsNone(self.composants.composant_utilisateur(self.resultat, self.tableau_plein))

    def test_reussi(self):
        self.assertIsNone(self.game.reussi())

    def test_start(self):
        self.assertIsNone(self.game.start(self.resultat, self.resultat))

    def test_game_over(self):
        self.assertIsNone(self.game.game_over())

    def test_melanger(self):
        self.assertTrue(self.composants.melanger(self.tableau_plein))
        self.assertFalse(self.composants.melanger(self.tableau_vide))


if __name__ == '__main__':
    unittest.main()
