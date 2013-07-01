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
        self.rect.center = (mousex, 480)
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
        self.shoot = False
	
    def update(self):
        #self.rect.centerx += self.dx
        if self.rect.right > 800:
            self.shoot = False
            self.reset()
		
        if self.shoot == True:
            self.rect.centerx += self.dx

        if self.shoot == False:
            bullet_position = pygame.mouse.get_pos()
            self.rect.centerx = bullet_position[0]
			
    def reset(self):
        self.rect.top = 475
        self.rect.centerx = -100 
        
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
    
def game():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Side ROLLER!")

    roller = Roller()
    enemyR = redEnemy()
    enemyP = peachEnemy()
    enemyW = whiteEnemy()
    background = Background()
    bullet = Bullet()
    scoreboard = Scoreboard()
    
    backgroundSprite = pygame.sprite.Group(background)
    badSprites = pygame.sprite.Group(enemyR, enemyP, enemyW)
    scoreSprite = pygame.sprite.Group(scoreboard)
    playerSprite = pygame.sprite.Group(roller)
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
                    roller.soundWaka.play()
                    bullet.shoot = True
		
        hitEnemys = pygame.sprite.spritecollide(roller, badSprites, False)
		
        if hitEnemys:
            roller.soundDeath.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print('Game over!')
                scoreboard.lives = 5
                scoreboard.score = 0
            for theEnemy in killEnemys:
                theEnemy.reset()

        killEnemys = pygame.sprite.spritecollide(bullet, badSprites, False)

        if killEnemys:
            roller.soundKill.play()
            scoreboard.score += 100
            bullet.shoot = False
            for theEnemy in killEnemys:
                theEnemy.reset()

        previousScore = 0
        if previousScore + 600 == scoreboard.score:
            previousScore = scoreboard.score
            enemyR.dx += 1
            enemyP.dx += 1
            enemyW.dx += 1
            print (previousScore)
            print (scoreboard.score)

			
        backgroundSprite.update()
        badSprites.update()
        scoreSprite.update()
        bulletSprite.update()
        playerSprite.update()

        backgroundSprite.draw(screen)
        badSprites.draw(screen)
        scoreSprite.draw(screen)
        bulletSprite.draw(screen)
        playerSprite.draw(screen)
        
        
        
        pygame.display.flip()
    
    roller.soundBackground.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True)
    return scoreboard.score
	
def instructions(score):
    roller = Roller()
    background = Background()
    
    allSprites = pygame.sprite.OrderedUpdates(background, roller)
    insFont = pygame.font.SysFont(None, 50)

    instructions = (
    "Mail Pilot.     Last score: %d" % score ,
    "Instructions:  You are a mail pilot,",
    "delivering mail to the islands.",
    "",
    "Fly over an island to drop the mail,",
    "but be careful not to fly too close",    
    "to the clouds. Your plane will fall ",
    "apart if it is hit by lightning too",
    "many times.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )

    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return donePlaying
        
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
	
if __name__ == "__main__":
    main()
