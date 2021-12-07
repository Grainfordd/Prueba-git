import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Juego')

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
color = YELLOW

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_UP:
                color = YELLOW
            if event.key == pygame.K_DOWN:
                color = BLUE

    screen.fill(pygame.Color(color))
    pygame.display.flip()

pygame.quit()
