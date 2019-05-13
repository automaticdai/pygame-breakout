import pygame
import sys
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

# -----------------------------
# CLASSES
class Actions(Enum):
    LEFT = 1
    RIGHT = 2
    FIRE = 3
    STOP = 4


class Ship:
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT - 100
    vx = 10
    width = 60
    height = 32
    fireLock = 0
    pic = pygame.image.load("./assets/images/ship.png")

    def __init__(self):
        pass

    def draw(self, display):
        pos = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        # pygame.draw.rect(display, (255, 0, 0), pos)
        display.blit(self.pic, pos)

    def is_open_fire(self):
        if self.fireLock == 0:
            return True
        else:
            return False


class Enemy:
    x = 0
    y = 0
    width = 48
    height = 32
    vx = 20
    vy = 80
    score = 30
    moveCnt = 50
    isHitWall = False
    isMoveY = False
    pic = pygame.image.load("./assets/images/InvaderA1.png")

    def __init__(self):
        pass

    def __init__(self, x0, y0, cnt):
        self.x = x0
        self.y = y0
        self.moveCnt = cnt

    def update(self):
        if self.moveCnt == 0:
            self.moveCnt = 50

            # if hit wall
            if (self.vx > 0 and self.x > SCREEN_WIDTH - self.width / 2) or (self.vx < 0 and self.x < 0 + self.width):
                self.isHitWall = True

            self.x = self.x + self.vx

        self.moveCnt = self.moveCnt - 1

    def move_y(self):
        self.vx = 0 - self.vx
        self.y = self.y + self.vy
        self.isHitWall = False

    def draw(self, display):
        pos = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        # pygame.draw.rect(display, (0, 255, 0), pos)
        display.blit(self.pic, pos)

    def is_hit(self, x, y):
        if (x >= self.x - self.width / 2) and (x <= self.x + self.width / 2) and (y >= self.y - self.width / 2) and (y <= self.y + self.width / 2):
            return True
        else:
            return False


class Bullet:
    x = 0
    y = 0
    vy = 0
    width = 6
    height = 17
    pic = pygame.image.load("./assets/images/bullet.png")

    def __init__(self):
        pass

    def __init__(self, x0, y0, vel):
        self.x = x0
        self.y = y0
        self.vy = vel

    def update(self):
        self.y = self.y + self.vy

    def draw(self, display):
        pos = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        # pygame.draw.rect(display, (200, 200, 200), pos)
        display.blit(self.pic, pos)

    def is_out_of_screen(self):
        if self.y < 0 or self.y > 1000:
            return True
        else:
            return False

# -----------------------------
# GLOBAL VARIABLES
action = Actions.STOP
score = 0
ship = Ship()
enemies = []
bullets = []


for i in range(5):
    for j in range(3):
        enemy = Enemy(100 * i + 100, 80 * j + 300, 30)
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
    gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
            if ship.is_open_fire():
                soundFire.play()
                bullet = Bullet(ship.x, ship.y, -10)
                bullets.append(bullet)
                ship.fireLock = 50

        if ship.fireLock != 0:
            ship.fireLock = ship.fireLock - 1

        # update all bullets
        for i in bullets:
            i.update()
            # hit any enemy?
            for j in enemies:
                if j.is_hit(i.x, i.y):
                    # destroy enemy
                    score = score + j.score
                    enemies.remove(j)
                    soundDestroyed.play()


                    # destroy bullet
                    bullets.remove(i)

            # out of screen?
            if i.is_out_of_screen():
                # destroy bullet
                bullets.remove(i)
                print(bullets)

        # update all enemies
        for i in enemies:
            i.update()

        for i in enemies:
            if i.isHitWall:
                for j in enemies:
                    j.move_y()

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
