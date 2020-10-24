import pygame
import math
from random import randint
import os
import time 

#initiates the pygame engine

pygame.init()

#Setting of basic Variables
WIDTH = 1152
HEIGHT = 648
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
SILVER = (192, 192, 192)
BROWN = (128,  0,   0)
COLOURS = [WHITE,BLUE,GREEN,RED,YELLOW,SILVER,BROWN]
#Setting main screen 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("cod")
clock = pygame.time.Clock()
#Opening the assets folder
game_folder = os.path.dirname(__file__)
asset_folder = os.path.join(game_folder, 'assets')

played_once = False

#Transforming and Scaling External Images
def scaleimage(width,height,img):
    image = pygame.image.load(os.path.join(asset_folder, img)).convert()
    image = pygame.transform.scale(image, (width, height))
    return image

image_size = 25
explosion_sound = pygame.mixer.Sound(os.path.join(asset_folder, 'Big_Explosion_Effect_Video_Mp4_HD_Sound-bhZs3ALdL7Y.wav'))
snowflake_img = scaleimage(10,10,'christmas_star_png_transparent_background_269546.png')
pizza_img = scaleimage(image_size,image_size,"cooked_pizza_on_a_transparent_background__by_prussiaart-dc50isb.png")
chicken_img = scaleimage(image_size,image_size,"105941_preview.png")
coke_img = scaleimage(image_size,image_size,"coca-cola-zagreb-croatia-january-l-alluminium-can-leading-soft-drink-brand-world-black-background-product-shot-63576244.png")
background_img = scaleimage(1152,648,"75fe7dce0f1d0eb.png")
background1_img = scaleimage(1152,648,"Preview_107.png")
option_border = scaleimage(500,100,"c94a5bb73628c4e.png")
background2_img = scaleimage(1152,648,"screen1.png")
OK_img = scaleimage(100,100,"ikesoksmall-01-2000x1200.png")


foods_img_list = [coke_img,pizza_img,chicken_img]

#Fonts and Text
def textrect(text,x,y):
    textbox = text.get_rect()
    textbox.centerx = x//2
    textbox.centery = y
    screen.blit(text,textbox)
    
Bazooka = pygame.font.SysFont("bazooka",30,True,False)
Bazooka1 = pygame.font.SysFont("bazooka",20,True,False)
text = Bazooka.render("E X P L O S I V E   A G A R I O", True, YELLOW)
text1 = Bazooka.render("P L A Y  G A M E", True, BLACK)
text2 = Bazooka.render("I N S T R U C T I O N S", True, BLACK)
text3 = Bazooka1.render("PLAYER 1: WASD TO MOVE", True, WHITE)
text4 = Bazooka1.render("PLAYER 2: ARROW KEYS TO MOVE", True, BLACK)
text5 = Bazooka1.render("EAT FOOD TO GROW, BE BIGGER THAN THE                                                 OTHER TO EAT THEM AND MAKE THEM EXPLODE", True, YELLOW)
text6 = Bazooka.render("PLAYER 1 WON", True, YELLOW)
text7 = Bazooka.render("PLAYER 2 WON", True, YELLOW)

#RESTART
def restart():
    for x in all_sprites:
        x.kill()


#START MENU
def menu():
    menu = False
    # reset1()
    # reset2()
    if played_once:
        restart()
    while not menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (border1.rect.left + 1) <= mouseposx and (border1.rect.right - 1) >= mouseposx and (border1.rect.top - 1) <= mouseposy and (border1.rect.bottom + 1) >= mouseposy:
                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    restart()
                    main_game()
                    menu = True
                if (border2.rect.left + 1) <= mouseposx and (border2.rect.right - 1) >= mouseposx and (border2.rect.top - 1) <= mouseposy and (border2.rect.bottom + 1) >= mouseposy:
                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    instructions()
                    menu = True
        
                
        screen.blit(background1_img,[0,0])
        textrect(text,WIDTH,100)
        textrect(text1,WIDTH,300)
        textrect(text2,WIDTH,450)
        border.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        pygame.display.flip()

#INSTRUCTIONS MENU
def instructions():
    instructions = False
    while not instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (border3.rect.left + 1) <= mouseposx and (border3.rect.right - 1) >= mouseposx and (border3.rect.top - 1) <= mouseposy and (border3.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        menu()
                        instructions = True
        screen.blit(background2_img,[0,0])
        textrect(text3,WIDTH//2, 100)
        textrect(text4,(2*(WIDTH - WIDTH//4)), HEIGHT - 100)
        textrect(text5,WIDTH,HEIGHT//2)
        border3.draw(screen)
        pygame.display.flip()

def explosion1(p1,p2):
    p1.rect.centery = HEIGHT//2
    p2.rect.centery = HEIGHT//2
    p1.rect.centerx = p1.radius
    p2.rect.centerx = WIDTH - p2.radius
    explosion = False
    while not explosion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (border3.rect.left + 1) <= mouseposx and (border3.rect.right - 1) >= mouseposx and (border3.rect.top - 1) <= mouseposy and (border3.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        p1.rect.centerx = 80
                        menu()
                        explosion = True
        screen.blit(background2_img,[0,0])
        p1.draw(screen)
        p2.draw(screen)
        if p1.rect.centerx != p2.rect.centerx:
            p1.rect.centerx += 1
        collide = pygame.sprite.collide_circle(p1,p2)
        if collide:
            screen.blit(background1_img,[0,0])
            border3.draw(screen)
            textrect(text6,WIDTH,50)
            pygame.mixer.Sound.play(explosion_sound)
            pygame.mixer.music.stop()
            
        pygame.display.flip()

def explosion2(p1,p2):
    p1.rect.centery = HEIGHT//2
    p2.rect.centery = HEIGHT//2
    p1.rect.centerx = p1.radius
    p2.rect.centerx = WIDTH - p2.radius
    explosion = False
    while not explosion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (border3.rect.left + 1) <= mouseposx and (border3.rect.right - 1) >= mouseposx and (border3.rect.top - 1) <= mouseposy and (border3.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        p2.rect.centerx = WIDTH - 80
                        menu()
                        explosion = True
        screen.blit(background2_img,[0,0])
        p1.draw(screen)
        p2.draw(screen)
        if p1.rect.centerx != p2.rect.centerx:
            p2.rect.centerx -= 1
        collide = pygame.sprite.collide_circle(p1,p2)
        if collide:
            screen.blit(background1_img,[0,0])
            border3.draw(screen)
            textrect(text7,WIDTH,50)
            pygame.mixer.Sound.play(explosion_sound)
            pygame.mixer.music.stop()
            
        pygame.display.flip()

        
        

class border(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 100
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class border1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 300
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class border2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 450
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class border3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = OK_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = HEIGHT//2
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

border = border()
border1 = border1()
border2 = border2()
border3 = border3()
    

class food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = foods_img_list[randint(0,2)]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(50,WIDTH-50)
        self.rect.centery = randint(50,HEIGHT-50)



class stars(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = snowflake_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0,WIDTH)
        self.rect.centery = randint(0,200)
        self.speedx = 1
        self.speedy = 3

    def update(self):
        if self.rect.left < 0:
            self.speedx *= -1
            self.rect.centerx += 5
        if self.rect.centerx > WIDTH:
            self.speedx *= -1
            self.rect.centerx -= 5
        if self.rect.bottom > HEIGHT + 10:
            self.rect.centery = randint(0,200)
            self.rect.centerx = randint(0,WIDTH)
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.color = WHITE
        self.radius = 50
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = 80
        self.rect.centery = HEIGHT//2

    def drawImage(self):
        ball_surface = pygame.Surface((self.radius*2,self.radius*2))
        ball_surface.fill(RED)
        ball_surface.set_colorkey(RED)
        pygame.draw.circle(ball_surface, self.color, [self.radius, self.radius], self.radius)
        return ball_surface.convert()


    def update(self):
        key = pygame.key.get_pressed()
        self.speedx = 0
        self.speedy = 0
        if key[pygame.K_w]:
            self.speedy = -10
        if key[pygame.K_s]:
            self.speedy = 10
        if key[pygame.K_a]:
            self.speedx = -10
        if key[pygame.K_d]:
            self.speedx = 10
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        if self.rect.left < -5:
            self.rect.centerx += 10
        if self.rect.right > WIDTH:
            self.rect.centerx -= 10
        if self.rect.top < 0:
            self.rect.centery += 10
        if self.rect.bottom > HEIGHT:
            self.rect.centery -= 10
        self.image = self.drawImage()

    def draw(self,screen):
        screen.blit(self.image,self.rect)


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.color = YELLOW
        self.radius = 50
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 80
        self.rect.centery = HEIGHT//2

    def drawImage(self):
        ball_surface = pygame.Surface((self.radius*2,self.radius*2))
        ball_surface.fill(RED)
        ball_surface.set_colorkey(RED)
        pygame.draw.circle(ball_surface, self.color, [self.radius, self.radius], self.radius)
        return ball_surface.convert()


    def update(self):
        key = pygame.key.get_pressed()
        self.speedx = 0
        self.speedy = 0
        if key[pygame.K_UP]:
            self.speedy = -10
        if key[pygame.K_DOWN]:
            self.speedy = 10
        if key[pygame.K_LEFT]:
            self.speedx = -10
        if key[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        if self.rect.left < -5:
            self.rect.centerx += 10
        if self.rect.right > WIDTH:
            self.rect.centerx -= 10
        if self.rect.top < 0:
            self.rect.centery += 10
        if self.rect.bottom >= HEIGHT:
            self.rect.centery -= 10
        self.image = self.drawImage()

    def draw(self,screen):
        screen.blit(self.image,self.rect)

player1 = Player()
player2 = Player2()

class Centre(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.color = RED
        self.radius = 5
        self.image = self.drawImage()
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery

    def drawImage(self):
        ball_surface = pygame.Surface((self.radius*2,self.radius*2))
        ball_surface.fill(self.color)
        ball_surface.set_colorkey(self.color)
        return ball_surface.convert()

    def update(self):
        self.radius = self.player.radius - 30
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery
        self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        self.image = self.drawImage()


class Centre2(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.color = RED
        self.radius = 5
        self.player = player
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery

    def drawImage(self):
        ball_surface = pygame.Surface((self.radius*2,self.radius*2))
        ball_surface.fill(self.color)
        ball_surface.set_colorkey(self.color)
        return ball_surface.convert()


    def update(self):
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery
        self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        self.image = self.drawImage()

# centre1 = centre()
# centre2 = centre2()
foods = pygame.sprite.Group()
players = pygame.sprite.Group()
# players.add(player1)
# players.add(player2)
all_sprites = pygame.sprite.Group()
# all_sprites.add(player1)
# all_sprites.add(player2)
# all_sprites.add(centre1)
# all_sprites.add(centre2)

def reset1(p1,p2,c1,c2):
    c1.radius = 5
    c2.radius = 5
    p1.radius = 50 
    p2.radius = 50
    p1.rect = p1.image.get_rect(center=(80,HEIGHT//2))
    p2.rect = p2.image.get_rect(center=(WIDTH-80,HEIGHT//2))
    players.add(p2)
    all_sprites.add(p2)
    all_sprites.add(c2)
    
def reset2(p1,p2,c1,c2):
    c1.radius = 5
    c2.radius = 5
    p1.radius = 50 
    p2.radius = 50
    p1.rect = p1.image.get_rect(center=(80,HEIGHT//2))
    p2.rect = p2.image.get_rect(center=(WIDTH-80,HEIGHT//2))
    players.add(p1)
    all_sprites.add(p1)
    all_sprites.add(c1)


    # all_sprites.add(x)


def main_game():
    for x in range(10):
        i = stars()
        all_sprites.add(i)
    overlap_once = False
    done = False
    for i in range(10):
        x = food()
        foods.add(x)
    player1 = Player()
    player2 = Player2()
    centre1 = Centre(player1)
    centre2 = Centre2(player2)
    players.add(player1)
    players.add(player2)
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(centre1)
    all_sprites.add(centre2)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        overlap = pygame.sprite.collide_circle(centre1, centre2)
        if overlap:
            if player1.radius > player2.radius and not overlap_once:
                player2.kill()
                centre2.kill()
                reset1(player1,player2,centre1,centre2)
                overlap_once = True
                done = True
                explosion1(player1,player2)

               
            elif player2.radius > player1.radius and not overlap_once:
                player1.kill()
                centre1.kill()
                reset2(player1,player2,centre1,centre2)
                overlap_once = True
                done = True
                explosion2(player1,player2)
            


        hits = pygame.sprite.groupcollide(players,foods,False,True,pygame.sprite.collide_circle)
        for collidedthing in hits:
            if collidedthing == player1:
                centre1.radius += 3
            if collidedthing == player2:
                centre2.radius += 3
            pygame.mixer.Sound.play(explosion_sound)
            pygame.mixer.music.stop()
            collidedthing.radius += 3
            collidedthing.rect = collidedthing.image.get_rect(center=(collidedthing.rect.centerx,collidedthing.rect.centery))
            x = food()
            foods.add(x)
            all_sprites.add(x)
            print(player1.radius,player2.radius)

        screen.blit(background_img,[0,0])
        foods.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(60)
        pygame.display.flip()


menu()
pygame.quit()
