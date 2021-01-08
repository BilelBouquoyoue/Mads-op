from game import Game


def main():
    # charger jeu
    game = Game()

    # boucle tant que condition vraie, le jeu continue
    while game.is_playing:
        if game.vie == 0:
            game.game_over()
            answer = game.YesNoQuestion('Voulez-vous recommencer le jeu ?(yes/no)')
            if answer == 'yes':
                print('Le jeu redémarre')
                game.start()
                main()
            elif answer == 'no':
                print("Le jeu va s'arréter!\n"
                      "Bonne journée à vous.")
                game.is_playing = False
                break
        else:
            game.jeu()


if __name__ == '__main__':
    main()
