import pygame

pygame.init()
pygame.font.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("3Blue1Brow: Collision")
font = pygame.font.SysFont(None, 30)
CLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

NUM_OF_COLLISIONS = 0

MASS_OF_OBJECT1 = 1000000
VELOCITY_OF_OBJECT1 = -50
POS_OF_OBJECT1 = 390
COLOR_OF_OBJECT1 = (100, 100, 100)
WIDTH_HEIGHT_OF_OBJECT1 = 300

MASS_OF_OBJECT2 = 1
VELOCITY_OF_OBJECT2 = 0
POS_OF_OBJECT2 = 300
COLOR_OF_OBJECT2 = (220, 220, 220)
WIDTH_HEIGHT_OF_OBJECT2 = 60

COUNTER = 1000
FPS = 1000


class Object:
    def __init__(self, mass, velocity, pos, color, width):
        self.mass = mass
        self.velocity = velocity
        self.pos = pos
        self.color = color
        self.width = width
        self.height = width


obj1 = Object(MASS_OF_OBJECT1, VELOCITY_OF_OBJECT1, POS_OF_OBJECT1, COLOR_OF_OBJECT1, WIDTH_HEIGHT_OF_OBJECT1)
obj2 = Object(MASS_OF_OBJECT2, VELOCITY_OF_OBJECT2, POS_OF_OBJECT2, COLOR_OF_OBJECT2, WIDTH_HEIGHT_OF_OBJECT2)


def calculate_collisions():
    global NUM_OF_COLLISIONS
    CLOCK.tick(FPS)
    dt1, dt2 = CLOCK.tick(FPS) / 1000, CLOCK.tick(COUNTER) / 1000
    dt = dt1 * dt2

    for i in range(COUNTER):
        obj1.pos += obj1.velocity * dt
        obj2.pos += obj2.velocity * dt
        if obj1.pos <= obj2.pos + 60:
            NUM_OF_COLLISIONS += 1
            old_vel, old_vel2 = obj1.velocity, obj2.velocity
            obj1.velocity = (obj1.mass - obj2.mass) / (obj1.mass + obj2.mass) * old_vel + (2 * obj2.mass) / (
                    obj1.mass + obj2.mass) * obj2.velocity
            obj2.velocity = (2 * obj1.mass) / (obj1.mass + obj2.mass) * old_vel + (obj2.mass - obj1.mass) / (
                    obj1.mass + obj2.mass) * old_vel2
        elif obj2.pos <= 40 and obj2.velocity < 0:
            obj2.velocity *= -1
            NUM_OF_COLLISIONS += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    calculate_collisions()

    pygame.Surface.fill(SCREEN, BLACK)

    pygame.draw.line(SCREEN, WHITE, (40, 450), (40, 0), 5) # vertical wall
    pygame.draw.line(SCREEN, WHITE, (800, 450), (40, 450), 2) # horizontal wall

    # draw obj
    pygame.draw.rect(SCREEN, obj1.color, pygame.Rect(obj1.pos, 450 - obj1.width, obj1.width, obj1.height))
    pygame.draw.rect(SCREEN, obj2.color, pygame.Rect(obj2.pos, 450 - obj2.width, obj2.width, obj2.height))

    # draw text
    textTBD = font.render("NUMBER OF COLLISIONS:" + str(NUM_OF_COLLISIONS), True, WHITE)
    SCREEN.blit(textTBD, (350, 30))

    pygame.display.flip()
