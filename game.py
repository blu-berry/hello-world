import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Display")
clock = pygame.time.Clock()

exit = False
x = 150
y = 150



pygame.draw.circle(gameDisplay, (200, 200, 200), (x, y), 15, 0)

while not exit:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 1
            gameDisplay.fill((0, 0, 0))
            if x < 0:
                x = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 1
            gameDisplay.fill((0, 0, 0))
            if x > 800:
                x = 800
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 1
            gameDisplay.fill((0, 0, 0))
            if y < 0:
                y = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 1
            gameDisplay.fill((0, 0, 0))
            if y > 600:
                y = 600

        print(x, y)
        pygame.draw.circle(gameDisplay, (200, 200, 200), (x, y), 15, 0)



    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
