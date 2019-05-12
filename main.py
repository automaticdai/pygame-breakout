import pygame
import sys
from enum import Enum


# -----------------------------
# CLASSES
class Actions(Enum):
    LEFT = 1
    RIGHT = 2
    FIRE = 3
    STOP = 4


class Ship:
    x = 800 / 2
    y = 900
    vx = 10
    width = 50
    height = 25

    def __init__(self):
        pass

    def draw(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))


class Enemy:
    x = 0
    y = 0
    width = 50
    height = 25
    vx = -20
    vy = 50
    moveCnt = 100

    def __init__(self):
        pass

    def __init__(self, x0, y0, cnt):
        self.x = x0
        self.y = y0
        self.moveCnt = cnt

    def update(self):
        if self.moveCnt == 0:
            self.moveCnt = 100
            self.x = self.x + self.vx
            # if hit wall
            # self.vx = 0 - self.vx;
            # self.y = self.y + self.vy
        self.moveCnt = self.moveCnt - 1

    def draw(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))


class Bullet:
    x = 0
    y = 0
    vy = 0
    width = 5
    height = 10

    def __init__(self):
        pass

    def __init__(self, x0, y0, vel):
        self.x = x0
        self.y = y0
        self.vy = vel

    def update(self):
        self.y = self.y + self.vy

    def draw(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))


# -----------------------------
# GLOBAL VARIABLES
action = Actions.STOP
score = 0
ship = Ship()
enemies = []
bullets = []

enemy = Enemy(500, 300, 30)
enemies.append(enemy)

if __name__ == "__main__":
    # -----------------------------
    # initialize pygame
    pygame.init()

    # load assets
    font = pygame.font.SysFont("comicsansms", 36)

    bg = pygame.image.load("./assets/images/bg1.jpg")

    soundFire = pygame.mixer.Sound("./assets/sounds/ShipBullet.wav")
    soundDestroyed = pygame.mixer.Sound("./assets/sounds/InvaderHit.wav")

    # -----------------------------
    # show display
    gameDisplay = pygame.display.set_mode((800, 1000))
    pygame.display.set_caption('Space Invader')

    clock = pygame.time.Clock()

    # -----------------------------
    # the main loop of the game
    crashed = False
    while not crashed:
        # -----------------------------
        # 1. handling events
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                crashed = True

            # keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    action = Actions.LEFT
                elif event.key == pygame.K_RIGHT:
                    action = Actions.RIGHT
                elif event.key == pygame.K_SPACE:
                    action = Actions.FIRE
            else:
                action = Actions.STOP

        # -----------------------------
        # 2. update states
        # update the ship
        if action == Actions.LEFT:
            ship.x = ship.x - ship.vx
        elif action == Actions.RIGHT:
            ship.x = ship.x + ship.vx
        elif action == Actions.FIRE:
            soundFire.play()
            bullet = Bullet(ship.x, ship.y, -10)
            bullets.append(bullet)
            pass

        # update all bullets
        for i in bullets:
            i.update()
            # hit any enemy?
                # destroy bullet
                # soundDestroyed.play()
            # out of screen?
                # destroy bullet
            pass

        # update all enemies
        for i in enemies:
            i.update()

        # handle scores
        score = score + 1

        # win? lose?

        # -----------------------------
        # 3. draw everything
        # background
        gameDisplay.blit(bg, (0, 0))

        # score
        text = font.render("Score: {:d}".format(score), True, (0, 128, 0))
        gameDisplay.blit(text, (0, 0))       #(0 + text.get_width(), 0 + text.get_height()))

        # draw the ship
        ship.draw(gameDisplay)

        # draw bullets
        for i in bullets:
            i.draw(gameDisplay)

        # draw enemies
        for i in enemies:
            i.draw(gameDisplay)

        # update display
        pygame.display.update()
        clock.tick(60)

    # -----------------------------
    # quit game
    pygame.quit()
    sys.exit()
