from playing import hangman
from textDisplay import textBox
from buttonDisplay import button
from colors import *
import pygame
import time
import random
 
class hangers:
    def __init__(self):
        pygame.init()                               #Initializing display and creating the pixel size for for the window
        self.display_width = 800
        self.display_height = 600
        self.CENTERED_XBUTTON = (self.display_width/2) - 100 #only works for button width 100
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("Hang me please!")   #Naming the window
        self.clock = pygame.time.Clock()
        self.menu = True

    def hard(self):                         #OPTIONS FUNCTIONS
        self.tries = 2
        self.catagory_menu()
    def medium(self):
        self.tries = 3
        self.catagory_menu()
    def easy(self):
        self.tries = 5
        self.catagory_menu()   
    def animals(self):
        self.cat = 'animals'
        self.start()
    def sports(self):
        self.cat = 'sports'
        self.start()
    def school(self):
        self.cat = 'school'
        self.start()
    def other(self):                        #END OF OPTIONS FUNCTIONS
        self.cat = 'other'
        self.start()

    def game_intro(self):                   #First screen that runs/ showing the name of the game and the game presentation
        intro = True
        part1 = True
        part2 = False
        part2a = False
        gameName = textBox(list(BLACK), 'Hangman', 100)
        presentation = textBox(list(WHITE), 'Presented by group elements', 58, 'comicsansms')
        #test = textBox(text = 'THIS IS A TEXT TEST', size = 200, center = True , ypixel = 200) #TESTING TEXT TO FIT TO SCREEN

        while intro:
            self.gameDisplay.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if part1:
                #gameName = textBox(gameName.color, 'Hangman', 100)     CHANGED RENDER TO textBox.displayBlit() FUNCTION SO WE DO NOT HAVE TO KEEP REINITIALIZING TEXTBOX ON LOOP
                gameName.displayBlit()
                #test.fitToScreen()                                         #TEXT FIT TO SCREEN
                #test.displayBlit()
                pygame.display.update()
                self.clock.tick(100)
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
                self.clock.tick(150)
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

    def game(self):                         #This is where the game loop begins
        mup = False
        self.menu = True
        title = textBox( text = 'Scuffed Hangman', size = 95, center = True, ypixel = 70, font= 'comicsansms')
        while self.menu:
            self.gameDisplay.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mup = True
                else:
                    mup = False
            
            title.displayBlit()
            button(60, "START",self.CENTERED_XBUTTON,(self.display_height/2)-50,200,100,GREEN,BRIGHT_GREEN,self.difficulty_menu, mup)
            button(80, "QUIT",self.CENTERED_XBUTTON,(self.display_height/2)+100,200,100,RED,BRIGHT_RED,pygame.quit, mup)
            pygame.display.update()
            self.clock.tick(60)
            
    def difficulty_menu(self):
        self.menu = True
        mup = False
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mup = True
                else:
                    mup = False
            self.gameDisplay.fill(WHITE)
            button(80, "Hard",self.CENTERED_XBUTTON,(self.display_height/2)-200,200,100,GRAY,BRIGHT_GRAY,self.hard, mup)
            button(55, "Medium",self.CENTERED_XBUTTON,(self.display_height/2)-50,200,100,GRAY,BRIGHT_GRAY,self.medium, mup)
            button(80, "Easy",self.CENTERED_XBUTTON,(self.display_height/2)+100,200,100,GRAY,BRIGHT_GRAY,self.easy, mup)
            button(35, "back", 0, 0, 75, 40, GRAY,BRIGHT_GRAY,self.game, mup)
            pygame.display.update()
            self.clock.tick(60)

    def catagory_menu(self):
        self.menu = True
        mup = False
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mup = True
                else:
                    mup = False
            self.gameDisplay.fill(WHITE)
            button(55, "Animals",self.CENTERED_XBUTTON, 50 ,200, 100,GRAY,BRIGHT_GRAY, self.animals, mup)
            button(55, "Sports",self.CENTERED_XBUTTON, 175 ,200,100,GRAY,BRIGHT_GRAY, self.sports, mup)
            button(55, "School",self.CENTERED_XBUTTON, 300 ,200,100,GRAY,BRIGHT_GRAY, self.school, mup)
            button(55, "Other",self.CENTERED_XBUTTON, 425 ,200,100,GRAY,BRIGHT_GRAY, self.other, mup)
            button(35, "back", 0, 0, 75, 40, GRAY,BRIGHT_GRAY,self.difficulty_menu, mup)
            pygame.display.update()
            self.clock.tick(60)

    def start(self):                        #The actual starts here and it's using the file playing
        mup = False
        self.play = hangman(self.tries)
        self.play.game()

        while self.play.win == True:
            self.gameDisplay.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mup = True
                else:
                    mup = False
            
            score = textBox(text = 'Score: ' + str(self.play.score), xpixel=0, ypixel=0, center = False)
            score.displayBlit()
            button(55, "Cont", self.CENTERED_XBUTTON, 150, 200, 100, GREEN, BRIGHT_GREEN, self.play.replay, mup)
            button(55, "Done", self.CENTERED_XBUTTON, 350, 200, 100, RED, BRIGHT_RED, self.highscore, mup)
            pygame.display.update()
            self.clock.tick(60)

        self.highscore()

    def highscore(self):                    #Always returns back to game function. get someone else to make the highscore screen to work?
        self.menu = False
        highscoreD = textBox(text = 'HIGHSCORE', ypixel = 100, size = 100)
        scores = []

        for i in range(5):
            scores.append(textBox(text = str(i + 1) + ' ----------', xpixel = 300, center = False, ypixel = 200 + (i * 75)))

        while self.menu != True:
            mup = False
            self.gameDisplay.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mup = True
                else:
                    mup = False

            highscoreD.displayBlit()
            for score in scores:
                score.displayBlit()
            button(55, 'Return', 600, 500, 200, 100, GRAY, BRIGHT_GRAY, self.game, mup)

            pygame.display.update()
            self.clock.tick(60)
    

meh = hangers()
meh.game_intro()
meh.game()
pygame.quit()
quit()