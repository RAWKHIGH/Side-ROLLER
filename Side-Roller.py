# https://github.com/RAWKHIGH/Side-ROLLER.git
# Name: Stephen McArthur
# Assinment 4
# Side ROLLER 

import pygame, random, time
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

        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.soundWaka = pygame.mixer.Sound("waka.wav")
            self.soundKill = pygame.mixer.Sound("eatghost.wav")
            self.soundDeath = pygame.mixer.Sound("death.wav")
            self.soundBackground = pygame.mixer.Sound("cursed_dream.wav")
            self.soundBackground.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, 500)
        
        
class redEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy_red.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 3
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.top = 470
        self.rect.centerx = 860

class peachEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy_peach.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 3
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.top = 470
        self.rect.centerx = 920
 
class whiteEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy_white.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 3
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.top = 470
        self.rect.centerx = 980
 
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gameBackground.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 2
        self.reset()
        
    def update(self):
        self.rect.left -= self.dy
        if self.rect.right <= 800:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0 
    
def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Side ROLLER!")

    roller = Roller()
    enemyR = redEnemy()
    enemyP = peachEnemy()
    enemyW = whiteEnemy()
    background = Background()
    
    goodSprites = pygame.sprite.Group(background, roller)
    badSprites = pygame.sprite.Group(enemyR, enemyP, enemyW)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        #check collisions
        hitEnemys = pygame.sprite.spritecollide(roller, badSprites, False)
        
        if hitEnemys:
            roller.soundDeath.play()
            for theEnemy in hitEnemys:
                theEnemy.reset()
        
        goodSprites.update()
        badSprites.update()
        goodSprites.draw(screen)
        badSprites.draw(screen)
        
        pygame.display.flip()
    
    roller.soundBackground.stop()

    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()