import pygame


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
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame: Breakout')

    clock = pygame.time.Clock()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
