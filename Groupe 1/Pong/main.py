import pygame
from Raquette import Raquette
from Balle import Balle
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong game")

joueur1 = Raquette(WHITE, 10, 100)
joueur1.rect.x = 20
joueur1.rect.y = 200

joueur2 = Raquette(WHITE, 10, 100)
joueur2.rect.x = 670
joueur2.rect.y = 200

balle = Balle(WHITE, 10, 10)
balle.rect.x = 345
balle.rect.y = 195

sprites_list = pygame.sprite.Group()
sprites_list.add(joueur1)
sprites_list.add(joueur2)
sprites_list.add(balle)

jeuEnCours = True
clock = pygame.time.Clock()

score1 = 0
score2 = 0

while jeuEnCours:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            jeuEnCours = False
    
    touches = pygame.key.get_pressed()
    if touches[pygame.K_z]:
        joueur1.moveUp(5)
    if touches[pygame.K_s]:
        joueur1.moveDown(5)
    if touches[pygame.K_UP]:
        joueur2.moveUp(5)
    if touches[pygame.K_DOWN]:
        joueur2.moveDown(5)

    sprites_list.update()

    if balle.rect.x>=690:
        score1 += 1
        balle.vitesse[0] = -balle.vitesse[0]
    if balle.rect.x<=0:
        score2 += 1
        balle.vitesse[0] = -balle.vitesse[0]
    if balle.rect.y>490:
        balle.vitesse[1] = -balle.vitesse[1]
    if balle.rect.y<0:
        balle.vitesse[1] = -balle.vitesse[1] 

    if pygame.sprite.collide_mask(balle, joueur1) or pygame.sprite.collide_mask(balle, joueur2):
        balle.rebond()

    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)
    sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (420,10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()