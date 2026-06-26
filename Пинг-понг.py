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

background = pg.transform.scale(pg.image.load('.jpg'), (W, H))

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
    finish = True
    win = False
    lose = False
    sound_played = False
    objs = []
    

    def update(self):
        pass
        
            



    def start(self):
        while game.run == True:
            self.update()
            btn_start.draw()

            display.update()
            clock.tick(FPS)

    def add_handler(self, obj):
        if obj in self.objs:
            self.objs.remove(obj)
        self.objs.append(obj)
            
        

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
        if keys_pressed[pg.K_W] and self.rect.y >= 0:
            self.rect.y += self.speed
        if keys_pressed[pg.K_S] and self.rect.y <= 500:
            self.rect.y += self.speed


class Player_2(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_UP] and self.rect.y >= 0:
            self.rect.y += self.speed
        if keys_pressed[pg.K_DOWN] and self.rect.y <= 500:
            self.rect.y += self.speed



class Ball(GameSprite):
    # colliderect == True -> умножаем x_speed и y_speed на -1
    pass
    self.x_speed = x_speed
    self.y_speed = y_speed






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

def end_game():
    game.run = False
    btn_exit.visible = False


btn_exit.set_on_click(end_game)
btn_start.set_on_click(start_level)


game.levels[0].reload()
btn_start.visible = True

while game.run == True:

    game.update()

    pg.display.update()
    clock.tick(FPS)