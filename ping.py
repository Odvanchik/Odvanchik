from random import randint
from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг Понг')
fon = transform.scale(image.load('sf2-banner.jpg'),(700,500))
window.blit(fon,(0,0))

game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed

fon = transform.scale(image.load('sf2-banner.jpg'), (980,680))
spriteplayer = Player('Leet_j.webp',850,400,10,90,150)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(fon,(0,0))

        spriteplayer.reset()
        spriteplayer.update()

    display.update()
  