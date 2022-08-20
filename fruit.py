import pygame
from pygame import Vector2
from random import randint
from config import *


class Fruit(pygame.sprite.Sprite):
    def __init__(self, pos: Vector2):
        self.image = pygame.image.load(SNAKE_MAIN_TILE)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft=(pos.x * TILE_SIZE, pos.y * TILE_SIZE))

    def getRect(self):
        return self.rect

    def newPos(self, pos, snakeBody):
        isClear = True
        for bodyTile in snakeBody:
            if bodyTile == pos:
                isClear = False
                break
        if isClear:
            self.rect.topleft = (pos.x * TILE_SIZE, pos.y * TILE_SIZE)
        else:
            return self.newPos(Vector2(randint(1, WINDOW_CELLS_X-1), randint(1, WINDOW_CELLS_Y-1)), snakeBody)

    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit(self.image, self.rect)
    