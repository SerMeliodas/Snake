import sys
import pygame 
from pygame import Vector2
from pygame.locals import *
from config import *
from random import randint
from snake import Snake
from fruit import Fruit
from scores import Scores


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 150)
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.fruit = Fruit(Vector2(4,4))
        self.scores = Scores()
        self.loose = False

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.SCREEN_UPDATE:
                self.snake.update()

            self.snake.input(event)

        if self.snake.getRect().colliderect(self.fruit.getRect()):
            self.snake.addBodyTile()
            self.fruit.newPos(Vector2(randint(1, WINDOW_CELLS_X-1), randint(1, WINDOW_CELLS_Y-1)), self.snake.getBody())
            self.scores.setScores(self.scores.getScores()+1)

    def run(self):
        while True:
            self.eventLoop()
            self.display.fill((20,10,20))
            self.snake.draw()
            self.fruit.draw()
            self.scores.draw()
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
