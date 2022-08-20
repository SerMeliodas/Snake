import pygame
from pygame import Vector2

from config import *


class Snake:
    def __init__(self):
        super().__init__()
        self.snakeBody = [Vector2(1, 2), Vector2(1, 3)]
        self.velocity = pygame.math.Vector2()

    def setVelocity(self, pos: tuple):
        self.velocity.x = pos[0]
        self.velocity.y = pos[1]

    def getBody(self):
        return self.snakeBody

    def getVelocity(self):
        return self.velocity

    def getRect(self):
        return pygame.Rect(int(self.snakeBody[0].x * TILE_SIZE ), int(self.snakeBody[0].y * TILE_SIZE ), TILE_SIZE, TILE_SIZE)

    def addBodyTile(self):
        self.snakeBody.insert(len(self.snakeBody),Vector2(self.snakeBody[0].x ,self.snakeBody[0].y))

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.snakeBody[0].y <= self.snakeBody[1].y:
                    self.setVelocity((0, -1))
            if event.key == pygame.K_s:
                if self.snakeBody[0].y >= self.snakeBody[1].y:
                    self.setVelocity((0, 1))
            if event.key == pygame.K_d:
                if self.snakeBody[0].x >= self.snakeBody[1].x:
                    self.setVelocity((1, 0))
            if event.key == pygame.K_a:
                if self.snakeBody[0].x <= self.snakeBody[1].x:
                    self.setVelocity((-1, 0))

        if (self.snakeBody[0].x == -1 or self.snakeBody[0].x == WINDOW_CELLS_X+1
            or self.snakeBody[0].y == -1 or self.snakeBody[0].y == WINDOW_CELLS_Y+1):
            self.snakeBody ==  [Vector2(1, 2), Vector2(1, 3), Vector2(1, 4)]

    def move(self):
        bodyCopy = self.snakeBody[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.velocity)
        self.snakeBody = bodyCopy[:]

    def draw_body(self, surface):
        for index, bodyTile in enumerate(self.snakeBody):
            x_pos = int(bodyTile.x * TILE_SIZE )
            y_pos = int(bodyTile.y * TILE_SIZE )

            rect = pygame.Rect(x_pos, y_pos, TILE_SIZE-3, TILE_SIZE-3)
            if index == 0:
                pygame.draw.rect(surface, pygame.Color("blue"), rect)
            else:
                pygame.draw.rect(surface, pygame.Color("white"), rect)

    def draw(self):
        surface = pygame.display.get_surface()
        self.draw_body(surface)
    
    def selfColide(self):
        pass
    def update(self):
        self.move()
        self.selfColide()
