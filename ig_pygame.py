import pygame as pg
import math
pg.init()

#generer la fenetre de jeu
pgd = pg.display
pgd.set_caption("The Mads Op")
screen = pgd.set_mode((1080, 720))

#background d'image
background = pg.image.load("assets/bg.jpg")

#chagement du logo
logo = pg.image.load("MadsOpLogo.png")
logo = pg.transform.scale(logo, (400, 400))
logo_rect = logo.get_rect()
logo_rect.x = math.ceil(screen.get_width() / 3)
logo_rect.y = math.ceil(screen.get_height() / 12)


#boutton de demarrage
play_button = pg.image.load("assets/button.png")
play_button = pg.transform.scale(play_button, (300, 113))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.69)
play_button_rect.y = math.ceil(screen.get_height() / 1.65)


running = True

#boucle tant que condition vrai
while running:

    #appliquer l'arriere plan
    screen.blit(background, (-100, -200))
    screen.blit(logo, logo_rect)
    screen.blit(play_button, play_button_rect)

    #mettre a jour l'ecran
    pgd.flip()

    #si l'utilisateur ferme la fenetre
    for event in pg.event.get():
        #que l'evenement est fermeture d'evenement
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            print("Fin de Jeu")