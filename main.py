import pygame

pygame.init()
CLOCK = pygame.time.Clock()
fps = 60
SCREEN_WIDTH = 800
PANEL = 100
SCREEN_HEIGHT = 400 + PANEL
new_var = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

background_image = pygame.image.load("images/background.png").convert_alpha()
panel_image = pygame.image.load("images/panel.png").convert_alpha()

#classes for fighets
class Player():
    def __init__(self, x, y, name, strength):
        self.x = x
        self.y = y
        self.name = name
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/player/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() *3, img.get_height()*3))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rectangle = self.image.get_rect()
        self.rectangle.center = (x, y)


    def draw(self):
        screen.blit(self.image, self.rectangle)

    def move_right(self):
        pass

    def move_left(self):
        pass
#creating class that inheirits from the player class
class Enemy(Player):
    def __init__(self, x, y, name, strength):
        super().__init__(x, y, name, strength)
        image = pygame.image.load("enemy/enemy.png")
        self.image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))


first_fighter = Player(200, SCREEN_HEIGHT/2, "player1", 10)
enemy1 = Enemy(600, 280, "enemy1", 5)
enemy2 = Enemy(700, 280, "enemy1", 5)
enemy_list = []
enemy_list.append(enemy1)
enemy_list.append(enemy2)


#function for backgroung image
def back_image():
    screen.blit(background_image,(0,0))

#function for panel image
def pan_image():
    screen.blit(panel_image,(0,SCREEN_HEIGHT - PANEL))

#keeping the windown open
playing = True
while playing:
    CLOCK.tick(fps)
    back_image()
    pan_image()
    for enemies in enemy_list:
        enemies.draw()

    first_fighter.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    pygame.display.update()

pygame.QUIT


