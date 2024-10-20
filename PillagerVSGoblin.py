#Welcome to Pillager Vs Goblin


import pygame
pygame.ver
pygame.init()

class player():
    #loading images
    walkRight = [
    pygame.image.load(r"firstResources/Sprite/R1.png"),
    pygame.image.load(r"firstResources/Sprite/R2.png"),
    pygame.image.load(r"firstResources/Sprite/R3.png"),
    pygame.image.load(r"firstResources/Sprite/R4.png"),
    pygame.image.load(r"firstResources/Sprite/R5.png"),
    pygame.image.load(r"firstResources/Sprite/R6.png"),
    pygame.image.load(r"firstResources/Sprite/R7.png"),
    pygame.image.load(r"firstResources/Sprite/R8.png"),
    pygame.image.load(r"firstResources/Sprite/R9.png")
    ]

    walkLeft = [
    pygame.image.load(r"firstResources/Sprite/L1.png"),
    pygame.image.load(r"firstResources/Sprite/L2.png"),
    pygame.image.load(r"firstResources/Sprite/L3.png"),
    pygame.image.load(r"firstResources/Sprite/L4.png"),
    pygame.image.load(r"firstResources/Sprite/L5.png"),
    pygame.image.load(r"firstResources/Sprite/L6.png"),
    pygame.image.load(r"firstResources/Sprite/L7.png"),
    pygame.image.load(r"firstResources/Sprite/L8.png"),
    pygame.image.load(r"firstResources/Sprite/L9.png")
    ]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0 
        self.standing = True
        self.hitbox = (self.x + 17, self.y, 28, 60) #x,y,width, height
        self.score = 0
        self.health = 2

    
    def draw(self):
        #27 so that there are 27 frames
        #go back t0 index walkcount 0 so 27 doesnt exceed
        if self.walkCount + 1 > 27:
            self.walkCount = 0 

        if not self.standing: 
            
            if self.left: 
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y)) #// will remove decimal from integer
                self.walkCount += 1 
            elif sprite.right: 
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
        else: 
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(self.walkLeft[0], (self.x, self.y))
            else:
                win.blit(character[0], (self.x, self.y))
        
        self.hitbox = (self.x + 17, self.y, 28, 60)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    
    def hit(self):
        print("hit")
        self.score += 1
    
    def collision(self):

        #setting position variables to reset sprite position when collided with goblin
        self.isJump = False
        self.jumpCount = 0
        self.x = 50
        self.y = 400
        self.walkCount = 0
        self.health -= 1 #loosing health when collided with gobling

        #telling player that they were hit by the goblin
        font1 = pygame.font.SysFont("comicsans", 30) 
        text = font1.render("You got hit!", 1, (200,0,0))
        win.blit(text, (screenWidth/2, screenHeight/2))
        pygame.display.update()

        #checking to end the game
        if self.health == 0:
            print("Dead")
            win.blit(bg[1], (0,0))
            # pygame.time.delay(2000)
            # pygame.quit()



        #this is a clock, this will wait 3 sec till resuming game
        #this clock also allows users to quit game if they dont want to wait 3 seconds
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        
        #now i need to write code as to check when golbin in in hitbox of sprite
        


class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = facing * 8

    #drawing the bullet with pygame.draw
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy():

    walkLeft = [
        pygame.image.load(r"firstResources/goon/L1E.png"),
        pygame.image.load(r"firstResources/goon/L2E.png"),
        pygame.image.load(r"firstResources/goon/L3E.png"),
        pygame.image.load(r"firstResources/goon/L4E.png"),
        pygame.image.load(r"firstResources/goon/L5E.png"),
        pygame.image.load(r"firstResources/goon/L6E.png"),
        pygame.image.load(r"firstResources/goon/L7E.png"),
        pygame.image.load(r"firstResources/goon/L8E.png"),
        pygame.image.load(r"firstResources/goon/L9E.png"),
        pygame.image.load(r"firstResources/goon/L10E.png"),
        pygame.image.load(r"firstResources/goon/L11E.png")
    ]

    walkRight = [
        pygame.image.load(r"firstResources/goon/R1E.png"),
        pygame.image.load(r"firstResources/goon/R2E.png"),
        pygame.image.load(r"firstResources/goon/R3E.png"),
        pygame.image.load(r"firstResources/goon/R4E.png"),
        pygame.image.load(r"firstResources/goon/R5E.png"),
        pygame.image.load(r"firstResources/goon/R6E.png"),
        pygame.image.load(r"firstResources/goon/R7E.png"),
        pygame.image.load(r"firstResources/goon/R8E.png"),
        pygame.image.load(r"firstResources/goon/R9E.png"),
        pygame.image.load(r"firstResources/goon/R10E.png"),
        pygame.image.load(r"firstResources/goon/R11E.png")
    ] 
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 17
        self.walkCount = 0 
        self.path = [self.x, self.end] #start and end of its path
        self.hitbox = (self.x + 17, self.y, 31, 57) #x,y,width, height
        self.score = 0 #keeps track of health, game over at 10 
        self.visible = True

    def draw(self, win): 
        self.move()

        #done to remove enemy after death
        if self.visible: 
            if self.walkCount + 1 > 33: 
                self.walkCount = 0
            
            #loading image rights
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else: 
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

            self.hitbox = (self.x + 17, self.y, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

            #drawwing health bar
            #full health bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 40, 10))
            #black health bar that takes over as he looses health
            pygame.draw.rect(win, (0,130,0), (self.hitbox[0], self.hitbox[1] - 20, 40 - (4 * sprite.score), 10))


    def move(self):
        #when moving right
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else: 
                self.vel = self.vel * -1
                self.walkCount = 0
        else: 
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else: 
                self.vel = self.vel * -1
                self.walkCount = 0 
        


#making window\
screenWidth = 852
screenHeight = 480
win = pygame.display.set_mode((screenWidth, screenHeight))

#loading images
bg = [pygame.image.load(r"firstResources/bg.jpg"), pygame.image.load(r"firstResources/GameOver.png")]
character = [pygame.image.load(r"firstResources/Sprite/standing.png")]

#loading sounds
bulletSound = pygame.mixer.Sound(r"firstResources/bullet.wav")
hitSound = pygame.mixer.Sound(r"firstResources/hit.wav")

backgroundSound = pygame.mixer.music.load(r"firstResources/music.mp3")
#continuously plays background music
pygame.mixer.music.play(-1)


#making a function for drawing all objects
def redraw():
    if sprite.score == 10 or goblin.score == 1 or sprite.health == 0:
        win.blit(bg[1], (0,0))
    else: 
        win.blit(bg[0], (0,0)) #setting background to image
        text = font.render("Score: " + str(sprite.score) + "/10", 1, (230,0,0))
        win.blit(text, (0,0))
        sprite.draw()
        goblin.draw(win)
    
    for bullet in bullets: 
        bullet.draw(win) 

    pygame.display.update()


#clock to set fps of game
clock = pygame.time.Clock()

#setting sprite
sprite = player(50, 400, 64, 64)


#main loop
font = pygame.font.SysFont("comicsans", 30, True, True) #settig font for score
run = True 
bullets = []
shootLoop = 0 #this is variable to make only 1 bullet come at once
goblin = enemy(300, 400, 64, 64, 800)

while run: 
    clock.tick(27)

    #checking if goblin collided wiwth sprite
    #this was the hitbox declaration: self.hitbox = (self.x + 17, self.y, 31, 57) #x,y,width, height
    if (sprite.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3]) and (sprite.hitbox[1] + sprite.hitbox[3] > goblin.hitbox[1]):
        if (sprite.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]) and (sprite.hitbox[0] + sprite.hitbox[2] > goblin.hitbox[0]):
            sprite.collision()
            hitSound.play()


    #checking for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if sprite.health == 0:
        sprite.score = 10

    #checking if sprite or goblin won the game
    if sprite.score == 10:
        print("Sprite Won")
        redraw()
        pygame.time.delay(3000)
        run = False                
                        
    elif goblin.score == 10:
        print("Enemy Won")
        redraw()
        pygame.time.delay(3000)
        run = False

    #shootLoops needs to be equal to be 0 for another bullet to be shot
    #this basically sets a timer along with the while loop
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 8: 
        shootLoop = 0  

    #making the bullets actually move and setting array to store all bullets

    for bullet in bullets: 
        #checking if bullet is in same y coordinate of hitbox
        #this was the hitbox declaration: self.hitbox = (self.x + 17, self.y, 31, 57) #x,y,width, height
        if (bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3]) and (bullet.y - bullet.radius > goblin.hitbox[1]):
            if (bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]) and (bullet.x - bullet.radius > goblin.hitbox[0]):
                sprite.hit()
                hitSound.play()
                #removing bullet after hit
                bullets.pop(bullets.index(bullet))


        #this is removing the bullet and moving the bullet
        if bullet.x < 852 and bullet.x > 0: 
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            #this deletes bullet from array at exact index
        


    
    #this continuously looks for key pressed and stores in array
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and shootLoop == 0: 
        bulletSound.play()
        
        if sprite.left:
            facing = -1
        elif sprite.right: 
            facing = 1 
            
        if len(bullets) < 6:
            bullets.append(projectile(round(sprite.x + sprite.width//2), round(sprite.y + sprite.height//2) ,7, (0,0,0), facing))

        shootLoop = 1

    if key[pygame.K_LEFT] and sprite.x > sprite.vel:
        sprite.x -= sprite.vel
        sprite.left = True
        sprite.right = False
        sprite.standing = False
    
    elif key[pygame.K_RIGHT] and sprite.x < (screenWidth - sprite.vel - sprite.width): 
        sprite.x += sprite.vel
        sprite.left = False
        sprite.right = True 
        sprite.standing = False

    else: 
        # sprite.left = False
        # sprite.right = False
        sprite.walkCount = 0
        sprite.standing = True


    if not sprite.isJump: 
        if key[pygame.K_UP]:
            sprite.isJump = True
            # sprite.right = False
            # sprite.left = False
            sprite.walkCount = 0 
            sprite.left = False
            sprite.right = False

    #configuring jump
    else:
        if sprite.jumpCount >= -10: 
            neg = 1
            if sprite.jumpCount > 0:
                neg = -1
            
            sprite.y+= (sprite.jumpCount**2) * 0.5 * neg
            sprite.jumpCount -= 1

        else: 
            sprite.jumpCount = 10
            sprite.isJump = False


    #drawing the character
    redraw()



#quitting 
pygame.quit()