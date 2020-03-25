from playing import hangman
from textDisplay import textBox
from buttonDisplay import button
from colors import *
import pygame
import time
import random

class options:
    def __init__(self, tries = 0, cat = ''):
        self.tries = tries
        self.cat = cat

    def hard(self):
        self.tries = 2
        catagory_menu(self)

    def medium(self):
        self.tries = 3
        catagory_menu(self)

    def easy(self):
        self.tries = 5
        catagory_menu(self)
    
    def animals(self):
        self.cat = 'animals'
        start(self)

    def sports(self):
        self.cat = 'sports'
        start(self)

    def school(self):
        self.cat = 'school'
        start(self)

    def other(self):
        self.cat = 'other'
        start(self)
 
pygame.init()                               #Initializing display and creating the pixel size for for the window
display_width = 800
display_height = 600
CENTERED_XBUTTON = (display_width/2) - 100 #only works for button width 100
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Let's hang!")   #Naming the window
clock = pygame.time.Clock()

def game_intro():                           #First screen that runs/ showing the name of the game and the game presentation
    intro = True
    part1 = True
    part2 = False
    part2a = False
    gameName = textBox(list(BLACK), 'Hangman', 100)
    presentation = textBox(list(WHITE), 'Presented by group elements', 58, 'comicsansms')
    #test = textBox(text = 'THIS IS A TEXT TEST', size = 200, center = True , ypixel = 200) #TESTING TEXT TO FIT TO SCREEN

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(WHITE)

        if part1:
            #gameName = textBox(gameName.color, 'Hangman', 100)     CHANGED RENDER TO textBox.displayBlit() FUNCTION SO WE DO NOT HAVE TO KEEP REINITIALIZING TEXTBOX ON LOOP
            gameName.displayBlit()
            #test.fitToScreen()                                         #TEXT FIT TO SCREEN
            #test.displayBlit()
            pygame.display.update()
            clock.tick(100)
            gameName.color[0] += 1
            gameName.color[1] += 1
            gameName.color[2] += 1

            if gameName.color[0] == WHITE[0]:
                part1 = False
                part2 = True

        elif part2:
            #presentation = textBox(presentation.color, 'Presented by group 2', 60, 'comicsansms')
            presentation.displayBlit()
            pygame.display.update()
            clock.tick(150)
            if presentation.color[0] > 0 and part2a == False:
                presentation.color[0] -= 1
                presentation.color[1] -= 1
                presentation.color[2] -= 1
                if presentation.color[0] == 0:
                    part2a = True
            elif part2a:
                presentation.color[0] += 1
                presentation.color[1] += 1
                presentation.color[2] += 1
                if presentation.color[0] == 255:
                    part2 = False
                    intro = False

def game():
    menu = True
    mup = False
    title = textBox( text = 'Scuffed Hangman', size = 95, center = True, ypixel = 70, font= 'comicsansms')
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mup = True
            else:
                mup = False
        gameDisplay.fill(WHITE)
        title.displayBlit()
        button(60, "START",CENTERED_XBUTTON,(display_height/2)-50,200,100,GREEN,BRIGHT_GREEN,difficulty_menu, mup)
        button(80, "QUIT",CENTERED_XBUTTON,(display_height/2)+100,200,100,RED,BRIGHT_RED,pygame.quit, mup)
        pygame.display.update()
        clock.tick(60)
        
def difficulty_menu():
    dmenu = True
    mup = False
    opt = options()
    while dmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mup = True
            else:
                mup = False
        gameDisplay.fill(WHITE)
        button(80, "Hard",CENTERED_XBUTTON,(display_height/2)-200,200,100,GRAY,BRIGHT_GRAY,opt.hard, mup)
        button(55, "Medium",CENTERED_XBUTTON,(display_height/2)-50,200,100,GRAY,BRIGHT_GRAY,opt.medium, mup)
        button(80, "Easy",CENTERED_XBUTTON,(display_height/2)+100,200,100,GRAY,BRIGHT_GRAY,opt.easy, mup)
        button(35, "back", 0, 0, 75, 40, GRAY,BRIGHT_GRAY,game, mup)
        pygame.display.update()
        clock.tick(60)

def catagory_menu(opt):
    cmenu = True
    mup = False
    while cmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mup = True
            else:
                mup = False
        gameDisplay.fill(WHITE)
        button(55, "Animals",CENTERED_XBUTTON, 50 ,200, 100,GRAY,BRIGHT_GRAY, opt.animals, mup)
        button(55, "Sports",CENTERED_XBUTTON, 175 ,200,100,GRAY,BRIGHT_GRAY, opt.sports, mup)
        button(55, "School",CENTERED_XBUTTON, 300 ,200,100,GRAY,BRIGHT_GRAY, opt.school, mup)
        button(55, "Other",CENTERED_XBUTTON, 425 ,200,100,GRAY,BRIGHT_GRAY, opt.other, mup)
        button(35, "back", 0, 0, 75, 40, GRAY,BRIGHT_GRAY,difficulty_menu, mup)
        pygame.display.update()
        clock.tick(60)

def start(opt):
    mup = False
    play = hangman(opt.tries)
    play.game()
    while play.win == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mup = True
            else:
                mup = False
        gameDisplay.fill(WHITE)
        score = textBox(text = 'Score: ' + str(play.score), xpixel=0, ypixel=0, center = False)
        score.displayBlit()
        button(55, "Again?", CENTERED_XBUTTON, 150, 200, 100, GREEN, BRIGHT_GREEN, play.replay, mup)
        button(55, "Done", CENTERED_XBUTTON, 350, 200, 100, RED, BRIGHT_RED, highscore, mup)
        pygame.display.update()
        clock.tick(60)
    highscore(play.score)

def highscore(score):
    ...


#game_intro()
game()
pygame.quit()
quit()