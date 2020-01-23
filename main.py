import pygame
import sys
import math
from pygame import mixer
import random
import shelve
import time

pygame.init()
screen = pygame.display.set_mode((800, 600)) #creates window screen
background = pygame.image.load('Game Assets\\background.png').convert_alpha() #background
background_level2 = pygame.image.load("Game Assets\\background2.png").convert_alpha()
background_level3 = pygame.image.load("Game Assets\\background3.png").convert_alpha()
main_menu = pygame.image.load("Game Assets\\main_menu.png").convert()
level_select_23locked = pygame.image.load("Game Assets\\level_select_23locked.png").convert()
level_select_3locked = pygame.image.load("Game Assets\\level_select_3locked.png").convert()
level_select_full = pygame.image.load("Game Assets\\level_select.png").convert()
mixer.music.load("Game Assets\\background_music.mp3") #loads background music
mixer.music.play(-1)
pygame.display.set_caption("Galactiblock") #icon and title
icon = pygame.image.load('Game Assets\\icon.png')
pygame.display.set_icon(icon)

class Block: #block class
    def __init__(self, Img, ImgX, ImgY):
        self.Img = Img
        self.ImgX = ImgX
        self.ImgY = ImgY

    def spawn(self, Img, ImgX, ImgY):
        screen.blit(Img, (ImgX, ImgY))

#PRESS SPACE TO BEGIN
start = False
press_start_font = pygame.font.Font('Game Assets\\slkscr.ttf', 42)

def press_to_start():
    space_start = press_start_font.render('PRESS SPACE TO BEGIN', True, (255,255,255))
    screen.blit(space_start, (130,280))

#UNLOCKED LEVEL CHECK
unlocked = shelve.open('game_data')
#unlocked['level_select'] = 1

#SCORE
score_value = 0
font = pygame.font.Font('Game Assets\\slkscr.ttf', 36)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

#RECORD
record = shelve.open('game_data')
highX = 10
highY = 100

def personal_record(x, y, level):
    high_s = font.render("Record: " + str(record[level]), True, (255, 255, 0))
    screen.blit(high_s, (x, y))

#MISSED
missed_value = 0 
missedX = 10
missedY = 55

def show_missed(x, y, num):
    missed = font.render("Missed: " + str(missed_value) + "/" + str(num), True, (255, 0, 0))
    screen.blit(missed, (x, y))

#GAME OVER
game_over_font = pygame.font.Font('Game Assets\\slkscr.ttf', 80)
def game_over():
    game_over_text = game_over_font.render('GAME OVER', True, (255,0,0))
    screen.blit(game_over_text, (160,250))
    reset_text = font.render("Press R to restart", True, (255, 255, 255))
    screen.blit(reset_text, (200, 350))
    return_text = font.render("Press Q to return", True, (255, 255, 255))
    screen.blit(return_text, (205, 400))

#INITIAL SPEED
IntervalA = 2.8
IntervalB = 3.8

#RED BLOCKS
redImg = pygame.image.load("Game Assets\\red_block.png").convert()
redX = 274
redY = random.randint(-1472, -128) #randomizes intial y-position
redChange = random.uniform(IntervalA, IntervalB) #randomizes intial speed
red_block = Block(redImg, redX, redY)

#SEA-FOAM BLOCKS
seafoamImg = pygame.image.load("Game Assets\\seafoam_block.png").convert()
seafoamX = 462
seafoamY = random.randint(-1472, -128) #randomizes intial y-position
seafoamChange = random.uniform(IntervalA, IntervalB) #randomizes initial speed
seafoam_block = Block(seafoamImg, seafoamX, seafoamY)

#JADE BLOCKS
jadeImg = pygame.image.load("Game Assets\\bluegreen_block.png").convert()
jadeX = 402
jadeY = random.randint(-1472, -128) #randomizes initial y-position
jadeChange = random.uniform(IntervalA, IntervalB) #randomizes initial speed
jade_block = Block(jadeImg, jadeX, jadeY)

#VIOLET BLOCKS
violetImg = pygame.image.load("Game Assets\\violet_block.png").convert()
violetX = 530
violetY = random.randint(-1472, -128) #randomizes initial y-position
violetChange = random.uniform(IntervalA, IntervalB) #randomizes initial speed
violet_block = Block(violetImg, violetX, violetY)

#LEFT BUTTON
leftButtonImg = pygame.image.load("Game Assets\\left_button.png").convert_alpha()
leftButtonImgPressed = pygame.image.load("Game Assets\\left_button_pressed.png")
leftB = [leftButtonImg, leftButtonImgPressed]
left_pressed = False

#RIGHT BUTTON
rightButtonImg = pygame.image.load("Game Assets\\right_button.png")
rightButtonImgPressed = pygame.image.load("Game Assets\\right_button_pressed.png")
rightB = [rightButtonImg, rightButtonImgPressed]
right_pressed = False

#UP BUTTON
upButtonImg = pygame.image.load("Game Assets\\up_button.png")
upButtonImgPressed = pygame.image.load("Game Assets\\up_button_pressed.png")
upB = [upButtonImg, upButtonImgPressed]
up_pressed = False

#DOWN BUTTON
downButtonImg = pygame.image.load("Game Assets\\down_button.png")
downButtonImgPressed = pygame.image.load("Game Assets\\down_button_pressed.png")
downB = [downButtonImg, downButtonImgPressed]
down_pressed = False

#COLLISION
def Collision(BlockX, BlockY, ButtonX, ButtonY):
    distance = math.sqrt((math.pow(BlockX-ButtonX,2)) + (math.pow(BlockY - ButtonY,2)))
    if distance < 72:
        return True
    else:
        return False

#CHANGE IN DIFFICULTY 
def increase_difficulty():
    global IntervalA
    global IntervalB
    if score_value % 10 == 0:
        IntervalA += .45
        IntervalB += .45
#RESET
def reset():
    global IntervalA, IntervalB, redY, redChange, seafoamY, seafoamChange, jadeChange, jadeY, violetY, violetChange
    IntervalA = 2.8
    IntervalB = 3.8
    redY = random.randint(-1472, -128) #randomizes intial y-position
    redChange = random.uniform(IntervalA, IntervalB) #randomizes intial speed
    seafoamY = random.randint(-1472, -128) #randomizes intial y-position
    seafoamChange = random.uniform(IntervalA, IntervalB) #randomizes intial speed
    jadeY = random.randint(-1472, -128)
    jadeChange = random.uniform(IntervalA, IntervalB)
    violetY = random.randint(-1472, -128)
    violetChange = random.uniform(IntervalA, IntervalB)

class GameStates: #master class
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class Menu(GameStates):
    def __init__(self):
        GameStates.__init__(self)
        self.next = "level_select"
    def pygame_event(self, event):
        play_button = pygame.Rect(330, 265, 145, 50)
        quit_button = pygame.Rect(335, 375, 130, 40)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
            if play_button.collidepoint(pos): #this checks whether or not the button was pressed
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                self.next = "level_select"
                self.done = True
            if quit_button.collidepoint(pos):
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                pygame.quit()
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(main_menu, (0, 0))

class LevelSelect(GameStates):
    def __init__(self):
        GameStates.__init__(self)
        self.next = "level1"
    def pygame_event(self, event):
        level_1 = pygame.Rect(50, 290, 190, 200)
        level_2 = pygame.Rect(315, 230, 175, 250)
        level_3 = pygame.Rect(575, 165, 160, 310)
        reset_prog = pygame.Rect(630, 493, 128, 64)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if level_1.collidepoint(pos):
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                self.next = "level1"
                self.done = True
            if level_2.collidepoint(pos):
                if unlocked['level_select'] == 2 or unlocked['level_select'] == 3:
                    select = mixer.Sound("Game Assets\\select.wav")
                    select.play()
                    time.sleep(.25)
                    self.next = "level2"
                    self.done = True
            if level_3.collidepoint(pos):
                if unlocked['level_select'] == 3:
                    select = mixer.Sound("Game Assets\\select.wav")
                    select.play()
                    time.sleep(.25)
                    self.next = 'level3'
                    self.done = True
            if reset_prog.collidepoint(pos):
                reset = mixer.Sound("Game Assets\\reset.wav")
                reset.play()
                unlocked['level_select'] = 1
                record['level1'] = 0
                record['level2'] = 0
                record['level3'] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                self.next = "main_menu"
                self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,0))
        if unlocked['level_select'] == 1:
            record['level2'] = 0
            screen.blit(level_select_23locked, (0, 0))
        if unlocked['level_select'] == 2:
            screen.blit(level_select_3locked, (0, 0))
        if unlocked['level_select'] == 3:
            screen.blit(level_select_full, (0, 0))

class Level1(GameStates):
    def __init__(self):
        GameStates.__init__(self)
        self.next = 'level_select'
    def pygame_event(self, event):
        global start, redY, seafoamY, missed_value, redChange, seafoamChange, score_value, left_pressed, right_pressed
        collisionRed = Collision(redX, redY, 306, 532) #checks for collisions between button and blocks
        collisionSeafoam = Collision(seafoamX, seafoamY, 494, 532)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
                if collisionRed:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    redY = random.randint(-320, -128)
                    increase_difficulty()
                    redChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_RIGHT:
                right_pressed = True
                if collisionSeafoam:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    seafoamY = random.randint(-320, -128)
                    increase_difficulty()
                    seafoamChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_r: #restart
                missed_value = 0
                score_value = 0
                reset()
            if event.key == pygame.K_q:
                missed_value = 0
                score_value = 0
                reset()
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                start = False
                self.done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False
    def update(self, screen, dt):
        self.draw(screen)
        global redY, seafoamY, missed_value, redChange, seafoamChange
        if start == False:
            press_to_start()
        if redY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            redY = random.randint(-1472, -128)
        if seafoamY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            seafoamY = random.randint(-1472, -128)
        if missed_value >= 4:
            game_over()
            redY = -64
            redChange = 0
            seafoamY = -64
            seafoamChange = 0
            if score_value > record['level1']: #updates record
                record['level1'] = score_value
            if record['level1'] >= 60:
                unlocked['level_select'] = 2
            if record['level1'] < 60:
                unlocked['level_select'] = 1

        while start: #updating positions
            redY += redChange 
            seafoamY += seafoamChange
            break

    def draw(self, screen):
        global left_pressed, right_pressed
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        red_block.spawn(redImg, redX, redY), seafoam_block.spawn(seafoamImg, seafoamX, seafoamY)
        if left_pressed == True:
            screen.blit(leftB[1], (274, 532)) 
        elif left_pressed == False:
            screen.blit(leftB[0], (274, 532))
        if right_pressed == True:
            screen.blit(rightB[1], (462, 532))
        elif right_pressed == False:
            screen.blit(rightB[0], (462, 532))
        show_score(textX, textY), show_missed(missedX, missedY, 4), personal_record(highX, highY, 'level1')
        

class Level2(GameStates):
    def __init__(self):
        GameStates.__init__(self)
        self.next = 'level_select'
    def pygame_event(self, event):
        global start, redY, seafoamY, missed_value, redChange, seafoamChange, score_value, jadeY, jadeChange, right_pressed, left_pressed, up_pressed
        collisionRed = Collision(redX, redY, 306, 532) #checks for collisions between button and blocks
        collisionJade = Collision(jadeX, jadeY, 434, 532)
        collisionSeafoam = Collision(530, seafoamY, 562, 532)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
                if collisionRed:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    redY = random.randint(-1472, -128)
                    increase_difficulty()
                    redChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_RIGHT:
                right_pressed = True
                if collisionSeafoam:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    seafoamY = random.randint(-1472, -128)
                    increase_difficulty()
                    seafoamChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_UP:
                up_pressed = True
                if collisionJade:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    jadeY = random.randint(-1472, -128)
                    increase_difficulty()
                    jadeChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_r: #restart
                missed_value = 0
                score_value = 0
                reset()
            if event.key == pygame.K_q:
                missed_value = 0
                score_value = 0
                reset()
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                start = False
                self.done = True
                self.next = "level_select"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_UP:
                up_pressed = False
    def update(self, screen, dt):
        self.draw(screen)
        global redY, seafoamY, missed_value, redChange, seafoamChange, jadeY, jadeChange
        if start == False:
            press_to_start()
        if redY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            redY = random.randint(-1472, -128)
        if seafoamY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            seafoamY = random.randint(-1472, -128)
        if jadeY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            jadeY = random.randint(-1472, -128)
        if missed_value >= 6:
            game_over()
            redY = -64
            redChange = 0
            seafoamY = -64
            jadeY = -64
            jadeChange = 0
            seafoamChange = 0
            if score_value > record['level2']: #updates record
                record['level2'] = score_value
            if record['level2'] >= 60:
                unlocked['level_select'] = 3

        while start: #updating positions
            redY += redChange 
            seafoamY += seafoamChange
            jadeY += jadeChange
            break

    def draw(self, screen):
        global left_pressed, right_pressed, up_pressed
        screen.fill((0,0,0))
        screen.blit(background_level2,(0,0))
        red_block.spawn(redImg, redX, redY), seafoam_block.spawn(seafoamImg, 530, seafoamY), jade_block.spawn(jadeImg, jadeX, jadeY)
        if left_pressed == True:
            screen.blit(leftB[1], (274, 532)) 
        elif left_pressed == False:
            screen.blit(leftB[0], (274, 532))
        if right_pressed == True:
            screen.blit(rightB[1], (530, 532))
        elif right_pressed == False:
            screen.blit(rightB[0], (530, 532))
        if up_pressed == True:
            screen.blit(upB[1], (402, 532))
        elif up_pressed == False:
            screen.blit(upB[0], (402, 532))
        show_score(textX, textY), show_missed(missedX, missedY, 6), personal_record(highX, highY, 'level2')

class Level3(GameStates):
    def __init__(self):
        GameStates.__init__(self)
        self.next = 'level_select'
    def pygame_event(self, event):
        global start, redY, seafoamY, missed_value, redChange, seafoamChange, score_value, jadeY, jadeChange, violetY, violetChange, left_pressed, right_pressed, up_pressed, down_pressed
        collisionRed = Collision(redX, redY, 306, 532) #checks for collisions between button and blocks
        collisionJade = Collision(jadeX, jadeY, 434, 532)
        collisionViolet = Collision(violetX, violetY, 562, 532)
        collisionSeafoam = Collision(658, seafoamY, 690, 532)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
                if collisionRed:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    redY = random.randint(-1472, -128)
                    increase_difficulty()
                    redChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_RIGHT:
                right_pressed = True
                if collisionSeafoam:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    seafoamY = random.randint(-1472, -128)
                    increase_difficulty()
                    seafoamChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_UP:
                up_pressed = True
                if collisionJade:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    jadeY = random.randint(-1472, -128)
                    increase_difficulty()
                    jadeChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_DOWN:
                down_pressed = True
                if collisionViolet:
                    sound = mixer.Sound('Game Assets\\collision.wav')
                    sound.play()
                    score_value += 1
                    violetY = random.randint(-1472, -128)
                    increase_difficulty()
                    violetChange = random.uniform(IntervalA, IntervalB)
            if event.key == pygame.K_r: #restart
                missed_value = 0
                score_value = 0
                reset()
            if event.key == pygame.K_q:
                missed_value = 0
                score_value = 0
                reset()
                select = mixer.Sound("Game Assets\\select.wav")
                select.play()
                time.sleep(.25)
                start = False
                self.done = True
                self.next = "level_select"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
    def update(self, screen, dt):
        self.draw(screen)
        global redY, seafoamY, missed_value, redChange, seafoamChange, jadeY, jadeChange, violetY, violetChange
        if start == False:
            press_to_start()
        if redY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            redY = random.randint(-1472, -128)
        if seafoamY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            seafoamY = random.randint(-1472, -128)
        if jadeY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            jadeY = random.randint(-1472, -128)
        if violetY >= 574:
            missed = mixer.Sound("Game Assets\\missed.wav")
            missed.play()
            missed_value += 1
            violetY = random.randint(-1472, -128)
        if missed_value >= 8:
            game_over()
            redY = -64
            redChange = 0
            seafoamY = -64
            jadeY = -64
            jadeChange = 0
            seafoamChange = 0
            violetY = -64
            violetChange = 0
            if score_value > record['level3']: #updates record
                record['level3'] = score_value
            if record['level3'] >= 60:
                unlocked['level_select'] = 3

        while start: #updating positions
            redY += redChange 
            seafoamY += seafoamChange
            jadeY += jadeChange
            violetY += violetChange
            break

    def draw(self, screen):
        global left_pressed, right_pressed, up_pressed, down_pressed
        screen.fill((0,0,0))
        screen.blit(background_level3,(0,0))
        red_block.spawn(redImg, redX, redY), seafoam_block.spawn(seafoamImg, 658, seafoamY), jade_block.spawn(jadeImg, jadeX, jadeY), violet_block.spawn(violetImg, violetX, violetY)
        if left_pressed == True:
            screen.blit(leftB[1], (274, 532)) 
        elif left_pressed == False:
            screen.blit(leftB[0], (274, 532))
        if right_pressed == True:
            screen.blit(rightB[1], (658, 532))
        elif right_pressed == False:
            screen.blit(rightB[0], (658, 532))
        if up_pressed == True:
            screen.blit(upB[1], (402, 532))
        elif up_pressed == False:
            screen.blit(upB[0], (402, 532))
        if down_pressed == True:
            screen.blit(downB[1], (530, 532))
        elif down_pressed == False:
            screen.blit(downB[0], (530, 532))
        show_score(textX, textY), show_missed(missedX, missedY, 8), personal_record(highX, highY, 'level3')

class GameControl:
    def __init__(self):
        self.__dict__.update()
        self.done = False
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
    def setup(self, levels, main_menu):
        self.levels = levels
        self.level_name = main_menu
        self.state = self.levels[self.level_name]
    def flip_state(self):
        self.state.done = False
        previous = self.level_name
        self.level_name = self.state.next
        self.state = self.levels[self.level_name]
        self.state.previous = previous
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.pygame_event(event)
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(120)/1000.0
            self.event_loop()
            self.update(delta_time)
            pygame.display.update()

game = GameControl()
levels = {
    'main_menu': Menu(),
    'level_select': LevelSelect(),
    'level1': Level1(),
    'level2': Level2(),
    'level3': Level3()
}

game.setup(levels, 'main_menu')
game.main_game_loop()
pygame.quit()
sys.exit()