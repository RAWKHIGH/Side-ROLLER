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
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 4

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > 800:
            self.reset()

    def reset(self):
        bullet_position = pygame.mouse.get_pos()
        self.rect.top = 450
        self.rect.centerx = bullet_position[0]
        
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
        self.rect.top = 450
        self.rect.centerx = random.randrange(800, 1500)

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
        self.rect.top = 450
        self.rect.centerx = random.randrange(800, 1500)
 
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
        self.rect.top = 450
        self.rect.centerx = random.randrange(800, 1500)

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "lives: %d score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
		
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gameBackground3.png")
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
    bullet = Bullet()
    scoreboard = Scoreboard()
    
    goodSprites = pygame.sprite.Group(background, roller)
    badSprites = pygame.sprite.Group(enemyR, enemyP, enemyW)
    scoreSprite = pygame.sprite.Group(scoreboard)
    bulletSprite = pygame.sprite.Group(bullet)
	
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bulletSprite.update()
                    bulletSprite.draw(screen)
                    roller.soundWaka.play()
		
        hitEnemys = pygame.sprite.spritecollide(roller, badSprites, False)
		
        if hitEnemys:
            roller.soundDeath.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print("Game over!")
                scoreboard.lives = 5
                scoreboard.score = 0
            for theEnemy in killEnemys:
                theEnemy.reset()

        #check collisions
        killEnemys = pygame.sprite.spritecollide(bullet, badSprites, False)

        if killEnemys:
            roller.soundKill.play()
            scoreboard.score += 100
            for theEnemy in killEnemys:
                theEnemy.reset()

        goodSprites.update()
        badSprites.update()
        scoreSprite.update()
		
        goodSprites.draw(screen)
        badSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    roller.soundBackground.stop()

    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
