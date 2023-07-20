import pygame

class Text ():
    

    def __init__(self ) :
        self.colors = {
            'WHITE ': (255, 255, 255),
            'BLACK' :(0, 0, 0)
        }
        self.font = pygame.font.Font(None, 36)
        

    def draw(self,screen,position, text,color):
        self.text = self.font.render(text, True, self.colors[color])
        screen.blit(self.text,position)