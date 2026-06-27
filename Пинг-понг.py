import pygame as pg
from random import randint
from time import *
pg.init()  

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pg.time.Clock()

HP = 3

W, H = 700, 500

background = pg.transform.scale(pg.image.load('поле.webp'), (W, H))

#создай окно игры
window = pg.display.set_mode((W, H))


#задай фон сцены
window.blit(background, (0, 0))

game = True

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color = None):
        self.rect = pg.Rect(x, y, width, height)                      
        self.fill_color = color
        self.spisok = []
    

class Lable(Area):
    def __init__(self, text, x=0, y=0, width=10, height=10, bg_color = None, text_color = BLACK, fsize = 25):
        super().__init__(x, y, width, height, bg_color)
        self.bg_color = bg_color
        self.set_text(text, text_color = text_color, fsize = fsize)
        self.fsize = fsize
        self.text_color = text_color

    def draw(self, shift_x=0, shift_y=0):
        if not self.bg_color is None:
            pg.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def set_text(self, text, fsize=None, text_color=None):
        if fsize is None:
            fsize = self.fsize
        if text_color is None:
            text_color = self.text_color
        self.text = text
        self.image = pg.font.Font(None, fsize).render(text, True, text_color)

class Game():
    run = True
    finish = False
    win = False
    lose = False
    sound_played = False
    objs = []
    events = []
    keys_pressed = {}


    

    def update(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                self.run = False

        window.blit(background, (0, 0))

        if self.finish == False:
            player_1.update()
            player_2.update()
            
            player_1.reset()
            player_2.reset()
            ball.reset()

        


        
            





class GameSprite(pg.sprite.Sprite):
    def __init__(self, image_name, x, y, w, h, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image_name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_s] and self.rect.y <= 420:
            self.rect.y += self.speed


class Player_2(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_DOWN] and self.rect.y <= 420:
            self.rect.y += self.speed



class Ball(GameSprite):
    def __init__(self, image_name, x, y, w, h, speed):
        super().__init__(image_name, x, y, w, h, speed)
        self.x_speed = speed
        self.y_speed = speed






class Button(Lable):
    func = None
    visible = False

    def set_on_click(self, func):
        self.func = func
        game.add_handler([self, 'on_click'])

    def on_click(self, x, y):
        if not self.func is None:
            self.func()

game = Game()

player_1 = Player_1('Платформа.png', 50, 150, 30, 80, 10)
player_2 = Player_2('Платформа.png', 150, 150, 30, 80, 10)
ball = Ball('Мяч.png', 200, 300, 40, 40, 30)





while game.run == True:

    game.update()

    pg.display.update()
    clock.tick(FPS)

    