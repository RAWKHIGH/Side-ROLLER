# https://github.com/RAWKHIGH/Side-ROLLER.git
# Name: Stephen McArthur
# Assinment 4
# Side ROLLER 

import pygame, random, time, math
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
            self.soundIntro = pygame.mixer.Sound("chemicalPlant.wav")
        
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
        
        self.dx = 6
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

class Obstical(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fallingBall.png")
        self.image = self.image.convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dy = 3
        self.attack = False
	
    def update(self):
        
        if self.rect.top > screen.get_height():
            #self.attack = False
            self.reset()
		
        if self.attack == True:
            self.rect.centery += self.dy

        if self.attack == False:
            self.rect.centery = -10
            self.rect.centerx = 400
			
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width()) 
		
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
    obstical0 = Obstical()
    obstical1 = Obstical()
    obstical2 = Obstical()
    obstical3 = Obstical()
    obstical4 = Obstical()

    scoreboard = Scoreboard()
    
    roller.soundBackground.play(-1)
	
    backgroundSprite = pygame.sprite.Group(background)
    badSprites = pygame.sprite.Group(enemyR, enemyP, enemyW)
    scoreSprite = pygame.sprite.Group(scoreboard)
    playerSprite = pygame.sprite.Group(roller)
    bulletSprite = pygame.sprite.Group(bullet)
    obsticalSprite = pygame.sprite.Group(obstical0,obstical1,obstical2,obstical3,obstical4)
	
    clock = pygame.time.Clock()
    keepGoing = True
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
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
                keepGoing = False
            for theEnemy in hitEnemys:
                theEnemy.reset()

        hitObstical = pygame.sprite.spritecollide(roller, obsticalSprite, False)
        if hitObstical:
            roller.soundDeath.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theEnemy in hitObstical:
                theEnemy.reset()
				
        killEnemys = pygame.sprite.spritecollide(bullet, badSprites, False)
        if killEnemys:
            roller.soundKill.play()
            scoreboard.score += 100
            bullet.shoot = False
            speedUp = False
            if scoreboard.score % 600 == 0 and scoreboard.score != 0:
                speedUp = True
                if speedUp == True:
                    speedUp = False
                    enemyR.dx = enemyR.dx + 1
                    enemyP.dx = enemyP.dx + 1
                    enemyW.dx = enemyW.dx + 1
                    print (enemyR.dx)
                    print (enemyP.dx)
                    print (enemyW.dx)
                    print (scoreboard.score)
            if scoreboard.score % 500 == 0 and scoreboard.score != 0:
                obstical0.attack = True
            if scoreboard.score % 1000 == 0 and scoreboard.score != 0:
                obstical0.attack = True
                obstical1.attack = True
                obstical2.attack = True
            if scoreboard.score % 2000 == 0 and scoreboard.score != 0:
                obstical0.attack = True
                obstical1.attack = True
                obstical2.attack = True
                obstical3.attack = True
                obstical4.attack = True
            for theEnemy in killEnemys:
                theEnemy.reset()
			
        backgroundSprite.update()
        badSprites.update()
        scoreSprite.update()
        bulletSprite.update()
        playerSprite.update()
        obsticalSprite.update()
		
        backgroundSprite.draw(screen)
        badSprites.draw(screen)
        scoreSprite.draw(screen)
        bulletSprite.draw(screen)
        playerSprite.draw(screen)
        obsticalSprite.draw(screen)
        
        
        pygame.display.flip()
   
    roller.soundBackground.stop()
    roller.soundWaka.stop()
    roller.soundDeath.stop()
    roller.soundKill.stop()

    #return mouse cursor
    pygame.mouse.set_visible(True)
    return scoreboard.score
	
def startScreen(score):
    roller = Roller()
    intro_image = pygame.image.load("Menu-DRAW.png").convert()
    pygame.display.set_caption("Intro")   
    roller.soundIntro.play(-1)
    screen.blit(intro_image, [0,0])
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
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
    

        pygame.display.flip()
    
    roller.soundIntro.stop()
    
    pygame.mouse.set_visible(True)
    return donePlaying

def gameOver(score):
    roller = Roller()
    outro_image = pygame.image.load("gameOver.png").convert()
    pygame.display.set_caption("Game Over!")   
    roller.soundIntro.play(-1)
    screen.blit(outro_image, [0,0])

    HSfile = open('HighScore.txt', 'r+')
    hs = HSfile.read()
    HSfile.close()
    print ('Old High Score ' + hs)
    HSfont = pygame.font.SysFont("None", 50)
    if str(score) >= hs:
        HSfile = open('HighScore.txt', 'r+')
        print ('NEW HIGH SCORE')
        HSfile.write(str(score)) 
        HSfile.close()
        MESStext = HSfont.render("New High Score!!", 1,(255,255,255))
        hScore = 1
    else:
        MESStext = HSfont.render("Good Job", 1,(255,255,255))
        hScore = 0
    HSfile = open('HighScore.txt', 'r+')
    hsN = HSfile.read()
    print ('New High Score ' + hsN)
    HStext = HSfont.render("High Score: "+ hsN, 1,(255,255,255))
    YStext = HSfont.render("Your Score: "+ str(score), 1,(255,255,255))
    if hScore == 0:
        screen.blit(MESStext, (300, 125))
    else:
        screen.blit(MESStext, (250, 125))
    screen.blit(HStext, (250, 250))
    screen.blit(YStext, (250, 300))
    HSfile.close()
	
    playAgain_image = pygame.image.load("playAgain.png").convert()
    playAgain_image.set_colorkey(black)
    screen.blit(playAgain_image, [199,420])
    playAgain_rect = pygame.draw.rect(screen, blue,(199,420, 200, 60,),2)
	
    quit_image = pygame.image.load("quit.png").convert()
    quit_image.set_colorkey(black)
    screen.blit(quit_image, [402,420])
    quit_rect = pygame.draw.rect(screen, blue,(402,420, 200, 60,),2)

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            mouse_x = mouse_position[0]
            mouse_y = mouse_position[1]
            print (mouse_position)
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= playAgain_rect.topleft[0] and mouse_y >= playAgain_rect.topleft[1]:
                    if mouse_x >= playAgain_rect.bottomleft[0] and mouse_y <= playAgain_rect.bottomleft[1]:
                        if mouse_x <= playAgain_rect.topright[0] and mouse_y >= playAgain_rect.topright[1]:
                            if mouse_x <= playAgain_rect.bottomright[0] and mouse_y <= playAgain_rect.bottomright[1]:
                                keepGoing = False
                                donePlaying = False
                                print ("Play Again")
                elif mouse_x >= quit_rect.topleft[0] and mouse_y >= quit_rect.topleft[1]:
                    if mouse_x >= quit_rect.bottomleft[0] and mouse_y <= quit_rect.bottomleft[1]:
                        if mouse_x <= quit_rect.topright[0] and mouse_y >= quit_rect.topright[1]:
                            if mouse_x <= quit_rect.bottomright[0] and mouse_y <= quit_rect.bottomright[1]:								
                                keepGoing = False
                                donePlaying = True
                                print ("Quit")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        pygame.display.flip()
    
    roller.soundIntro.stop()
    
    pygame.mouse.set_visible(True)
    return donePlaying
	
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = startScreen(score)
        if not donePlaying:
            score = game()
            donePlaying = gameOver(score)
if __name__ == "__main__":
    main()
