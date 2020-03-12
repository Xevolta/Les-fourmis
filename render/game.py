import pygame
import sys

from Class.Game import Game
class Lunch:
    def __init__(self):
        self.game = Game()
        self.quit= [(20,650),(110,50)]
        self.buttonBack = pygame.Rect((20,10),(110,50))
        self.TextBack = pygame.font.Font('asset/font/punch.ttf',25).render('Quit',True,(0,0,0),)
        self.rectBack = self.TextBack.get_rect()
        self.centerBack = self.rectBack.center



    def lunch(self,screen):
        while True:
            game = self.game
            background = pygame.image.load('asset/back/back.png')  # Met le fond
            screen.fill(0)
            screen.blit(background, (0, 0))  # Met le back
            screen.blit(self.game.player.playerImage, game.player.rect)  # Met le joueurerbas
            screen.blit(self.TextBack, self.centerBack)
            if game.press.get(
                pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():  # si la touche                                                                                             # fleche droite est appyer j'avance si je cogne la bordure je m'arrete
                game.player.move_r()
            elif game.press.get(pygame.K_LEFT) and game.player.rect.x > 0:  # si la touche fleche gauche est appyer j'avance
                game.player.move_l()
            elif game.press.get(pygame.K_UP) and game.player.rect.y > 0:  # si la touche fleche haut est appyer j'avance
                game.player.move_u()
            elif game.press.get(
                pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():  # si la touche
                game.player.move_d()

            pygame.display.flip()  # Mise a jours ecran*


            for event in pygame.event.get():  # Get les event
                if event.type == pygame.QUIT:  # Si l'event quit est lance je ferme le jeu
                    pygame.quit()  # Fermeture du jeux
                    print('Fermeture... ')  # Envoi en console
                    sys.exit(0)  # ferme le programme
                elif event.type == pygame.KEYDOWN:  # Si une touche est appuyer
                    game.press[event.key] = True  # Je prend le numeros de la touche et je dit qu'elle est vrai pour qu'elle puisse
                                   # execute (va avec le code un peux plus en haut)
                elif event.type == pygame.KEYUP:  # Si une touche est relache
                    game.press[event.key] = False  # Je met la touche en false pour arreter l'execution
                elif event.type == pygame.MOUSEBUTTONUP:  # quand je relache le bouton
                    if event.button == 1:  # 1= clique gauche
                        if self.buttonBack.collidepoint(event.pos):
                            pygame.quit()  # Fermeture du jeux
                            print('Fermeture... ')  # Envoi en console
                            sys.exit(0)  # ferme le programme