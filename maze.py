from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_speed, player_image):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 625:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((124, 205, 50))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

background  = transform.scale(image.load('background.jpg'), (700, 500))
hero = Player(50, 300, 7, 'hero.png')
cyborg = Enemy(630, 250, 5, 'cyborg.png')
treasure = GameSprite(600, 400, 0, 'treasure.png')
wall_1 = Wall(150, 0, 10, 390)
wall_2 = Wall(260, 300, 10, 200)
wall_3 = Wall(150, 200, 220, 10)
wall_4 = Wall(360, 200, 10, 190)
wall_5 = Wall(460, 80, 10, 430)
wall_6 = Wall(250, 80, 300, 10)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60

game = True

wall = []
wall.append(wall_1)
wall.append(wall_2)
wall.append(wall_3)
wall.append(wall_4)
wall.append(wall_5)
wall.append(wall_6)

finish = False
font.init()
font = font.SysFont('Arial', 70)
win = font.render(
    'YOY WIN!', True, (255, 215, 0)
)
lose = font.render(
    'YOY LOSE!', True, (255, 0, 0)
)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    for i in wall:
        i.draw_wall()

    if not finish:
        treasure.reset()
        hero.update()
        hero.reset()
        cyborg.update()
        cyborg.reset()

        if sprite.collide_rect(hero, treasure):
            finish = True
            window.blit(win, (200, 200))
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall_1) or sprite.collide_rect(hero, wall_2) or sprite.collide_rect(hero, wall_3) or sprite.collide_rect(hero, wall_4) or sprite.collide_rect(hero, wall_5) or sprite.collide_rect(hero, wall_6):
            finish = True
            window.blit(lose, (200, 200))
        display.update()
        clock.tick(FPS)