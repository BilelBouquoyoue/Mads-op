from game import Game


def main():
    # charger jeu
    game = Game()

    # boucle tant que condition vraie, le jeu continue
    while game.en_jeu:
        if game.vie == 0:
            game.game_over()
            answer = game.yes_no_question('Voulez-vous recommencer le jeu ?(yes/no)')
            if answer == 'yes':
                print('Le jeu redémarre')
                game.start()
                main()
            elif answer == 'no':
                print("Le jeu va s'arréter!\n"
                      "Bonne journée à vous.")
                game.en_jeu = False
                break
        else:
            game.jeu()


if __name__ == '__main__':
    main()
