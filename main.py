import pygame
import sys

class Pad:
    x = 0
    y = 0

    def __init__(self):
        pass


class Brick:
    x = 0
    y = 0

    def __init__(self):
        pass


class Ball:
    x = 0
    y = 0
    vx = 0
    vy = 0

    def __init__(self):
        pass


class Game:
    score = 0

    def __init__(self):
        pass


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('Pygame: Breakout')

    clock = pygame.time.Clock()

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                pass
            elif keys[pygame.K_RIGHT]:
                pass
            elif keys[pygame.K_UP]:
                pass

        pygame.draw.rect(gameDisplay, (255, 0, 0), (0, 0, 100, 100))
        pygame.display.update()
        clock.tick(60)

        #if event.type == QUIT:

    pygame.quit()
    sys.exit()
