import pygame


def commencement():
    pygame.init()
    pygame.display.set_caption("MAD'S Operation")
    screen = pygame.display.set_mode((1080, 720))

    background = pygame.image.load('assets/ecranTitre.png')

    running = True

    # boucle qui maintient la fenetre
    while running:

        # appliquer arriere plan
        screen.blit(background, (0, 0))

        # mettre a jour l'écran
        pygame.display.flip()

        # si le joueur ferme cette fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture de la fenêtre de jeu")


if __name__ == '__main__':
    commencement()
