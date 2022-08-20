import pygame 


class Scores:
    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans Ms', 30) 
        self.scores = 0
        self.surface = pygame.display.get_surface()

    def draw(self):
        text = self.font.render(str(self.scores), False, (255, 255, 255))
        self.surface.blit(text, (10, 10))
    
    def getScores(self):
        return self.scores

    def setScores(self, scores):
        self.scores = scores
