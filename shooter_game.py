#Создай собственный Шутер!

from pygame import *
from random import randint 
font.init()
window = display.set_mode((700, 500))
display.set_caption('Maze')
background = transform.scale(image.load('underwater.jpg'), (700, 500))
win_width = 700
win_height = 500
lost = 0 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',heroe.rect.centerx,heroe.rect.y,3)
        bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
    
    
class Bomb(GameSprite):
    def update(self):
        self.rect.y += self.speed
            

heroe = Player('submarine.png',0,420,3)


class Enemy(Player):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
bullets_schet = 0
bombs = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
timer = 150
timer2 = 400
win_streak = 0
restart = 400
player_lives = 3
clock = time.Clock()
FPS = 60
timer3 = 100
rel_time = False
game = True
finish = True
bullet_timer = 300
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        window.blit(background,(0,0))
        heroe.reset()
        heroe.move()

        monsters.draw(window)
        monsters.update()
        
        bullets.draw(window)
        bullets.update()

        bombs.draw(window)
        bombs.update()

        text_lose = font.Font(None, 36).render('Пропущено: '+ str(lost),1,(255,255,255))

        window.blit(text_lose, (0,40))

        text_lives = font.Font(None, 36).render('Жизни: '+ str(player_lives),1,(255,255,255))
        window.blit(text_lives,(585,0))


        if timer == 0:
            timer = 150

            monsters.add(Enemy('enemy.png',randint(50,650),-50,2))
        

        else:
            timer -= 1

        if timer2 == 0 :
            timer2 = 400
            bombs.add(Bomb('bomb.png',randint(50,650),-50,2))
        else:
            timer2 -= 1



        collides = sprite.groupcollide(monsters, bullets, True,True)
        collide2 =  sprite.spritecollide(heroe, bombs, True)
        if collide2:
            player_lives -= 1
            if player_lives == 0:
                finish = False
                background = transform.scale(image.load('underwater.jpg'), (700, 500))
                font1 = font.SysFont("Arial", 75)
                window.blit(background, (0, 0))
                txtsurf = font1.render("You lost", True, (255,255,255))
                window.blit(txtsurf,(200,200))



            
        for i in collides:
            win_streak += 1
            if win_streak == 10:
                finish = False
                background = transform.scale(image.load('underwater.jpg'), (700, 500))
                font1 = font.SysFont("Arial", 75)
                window.blit(background, (0, 0))
                txtsurf = font1.render("You win", True, (255,255,255))
                window.blit(txtsurf,(200,200))

        if lost == 5 :
            finish = False
            background = transform.scale(image.load('underwater.jpg'), (700, 500))
            font1 = font.SysFont("Arial", 75)
            window.blit(background, (0, 0))
            txtsurf = font1.render("You lost", True, (255,255,255))
            window.blit(txtsurf,(200,200))

        if finish == False:
            if restart == 0:   
                finish = True
                win_streak = 0
                player_lives = 3
                lost = 0
            else:
                restart -= 1
            



        text_win = font.Font(None, 36).render('Счет: '+ str(win_streak),1,(255,255,255))
        window.blit(text_win,(0,0))
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if bullets_schet < 5 and rel_time == False:
                        heroe.fire()
                        bullets_schet += 1
                    if bullets_schet >= 5:
                        rel_time = True

    if rel_time == True:
        if bullet_timer == 0:
            print(222)
            bullet_timer=300
            bullets_schet = 0
            rel_time = False
        else:
            bullet_timer -= 1 
            
                            



                    
                    


                    
                    
                    

                    
                        

    clock.tick(FPS)
    display.update()
