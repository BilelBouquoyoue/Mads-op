from game import Game


def main():
    # charger jeu
    game = Game()

    # boucle tant que condition vraie, le jeu continue
    while game.en_jeu:
        if game.vie == 0:
            game.game_over()
            answer = game.oui_non_question('Voulez-vous recommencer le jeu ?(oui/non)')
            if answer == 'oui':
                game.composants.affichage_console('démarrage')
                game.start()
                main()
            elif answer == 'non':
                game.composants.affichage_console('stop')
                game.en_jeu = False
                break
        else:
            game.jeu()


if __name__ == '__main__':
    main()
