import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FRUIT SLAYER")

running = True


bg=pygame.image.load('fruitbg.jpg')
bg=pygame.transform.scale(bg,(800,600))

# fruit = pygame.image.load('assets/apple.png')
# fruit = pygame.transform.scale(fruit,(100,100))
#
# fruit_half = pygame.image.load('assets/apple-half.png')
# fruit_half = pygame.transform.scale(fruit_half,(100,100))
#
# fruit1 = pygame.image.load('assets/lemon.png')
# fruit1 = pygame.transform.scale(fruit1,(100,100))
#
# fruit_half1 = pygame.image.load('assets/lemon-half.png')
# fruit_half1 = pygame.transform.scale(fruit_half1,(70,80))
#
#
# fruit_x = 100
# fruit_y = 100
#
# fruit1_x = 200
# fruit1_y = 200

fruit_names = ['lemon', 'apple', 'pear', 'egg', 'mushroom', 'sausage', 'avocado', 'coconut', 'onion','bomb']

full_images = {}
half_images = {}

for name in fruit_names:
    full = pygame.image.load('assets/' + name + '.png')
    half = pygame.image.load('assets/' + name + '-half.png')

    full_images[name] = pygame.transform.scale(full, (70, 80))
    half_images[name] = pygame.transform.scale(half, (70, 80))

print(full_images)
print(half_images)

fruits=[]
spawn_timer=0
score=0
lives=3


def add_fruit(fruit_list):
    name=random.choice(fruit_names)
    x = random.randint(50,750)
    y = 750
    v = -random.randint(20,28)
    g = 0.5

    fruit = {
        'name': name,
        'x': x,
        'y': y,
        'v':v,
        'g':g,
        'cut':False,
        'timer':0
    }
    fruit_list.append(fruit)
    print(fruit_list)

def draw_fruit(fruit_list):
    for fruit in fruit_list:
        name=fruit['name']
        x = fruit['x']
        y = fruit['y']
        if fruit['cut']==True:
            img = half_images[name]
        else:
            img = full_images[name]

        print(name)

        if name=='bomb':
            img=pygame.transform.scale(img,(90,100))

        screen.blit(img,(x,y))

def move_fruit(fruit_list):
    for fruit in fruit_list:
        fruit['v']+=fruit['g']
        fruit['y']+=fruit['v']

def check_click(fruit_list,pos,score,lives):
    fx,fy=pos

    for fruit in fruit_list:
        if not fruit['cut'] and fruit['name'] != 'bomb':
            if fruit['x'] < fx < fruit['x'] + 70 and fruit['y'] < fy < fruit['y']+80:
                fruit['cut']=True
                fruit['timer']=10
                score += 1
        if not fruit['cut'] and fruit['name'] == 'bomb':
            if fruit['x'] < fx < fruit['x'] + 70 and fruit['y'] < fy < fruit['y']+80:
                fruit['cut']=True
                fruit['timer']=10
                lives-=1

    return score,lives

background_color = (50, 20, 10)
def game_score(score):
    font=pygame.font.SysFont('comic sans ms',35)
    score_text='Score:'+ str(score)
    text=font.render(score_text,True,'white')
    screen.blit(text,(70,50))

def game_lives(lives):
    font=pygame.font.SysFont('comic sans ms',35)
    lives_text='lives:'+ str(lives)
    text=font.render(lives_text,True,'white')
    screen.blit(text,(230,50))

while running:
    pygame.time.delay(30)
    screen.fill((30,30,30))

    spawn_timer +=1

    if spawn_timer > 50:
        add_fruit(fruits)
        spawn_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            score,lives=check_click(fruits,pygame.mouse.get_pos(),score,lives)
            if lives <= 0:
                running = False
                font = pygame.font.SysFont('impact', 72)
                text = font.render('Game Over! ', True, 'red')
                screen.blit(text, (245,260))
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()

    screen.blit(bg,(0,0))

    # screen.blit(half_images['onion'], (200, 100))
    # screen.blit(full_images['apple'], (300, 100))
    # screen.blit(half_images['apple'], (400, 100))
    # screen.blit(full_images['egg'], (500, 100))
    # screen.blit(half_images['egg'], (600, 100))
    # screen.blit(full_images['coconut'], (700, 100))
    # screen.blit(half_images['coconut'], (100, 200))
    # screen.blit(full_images['mushroom'], (800, 200))
    # screen.blit(half_images['mushroom'], (200, 100))
    # screen.blit(full_images['pear'], (100, 100))
    # screen.blit(half_images['pear'], (200, 100))
    # screen.blit(full_images['lemon'], (100, 100))
    # screen.blit(half_images['lemon'], (200, 100))
    # screen.blit(full_images['avocado'], (100, 100))
    # screen.blit(half_images['avocado'], (444, 100))
    # screen.blit(full_images['sausage'], (100, 100))
    # screen.blit(half_images['sausage'], (300, 200))
    # screen.blit(full_images['onion'], (100, 100))

    move_fruit(fruits)
    draw_fruit(fruits)
    game_score(score)
    game_lives(lives)
    pygame.display.update()