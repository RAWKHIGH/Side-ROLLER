# https://github.com/RAWKHIGH/Side-ROLLER.git
# Name: Stephen McArthur
# Assinment 4
# Side ROLLER 

import pygame, random
pygame.init()

screen = pygame.display.set_mode((800, 600))

#            R    G    B
white    = (255, 255, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
yellow   = (255, 255,   0)
orange   = (255, 128,   0)
purple   = (255,   0, 255)
black    = (   0,   0,  0)


class Roller(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("roller.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(white)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, 500)
        
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy_red.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 2
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.top = 470
        self.rect.centerx = 860
    
    
def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mail Pilot! mpIsland - adding the Island")

    background = pygame.image.load("gameBackground.png").convert()
    screen.blit(background, (0, 0))
    roller = Roller()
    enemy = Enemy()
    
    allSprites = pygame.sprite.Group(enemy, roller)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()