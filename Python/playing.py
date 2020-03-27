from textDisplay import textBox
from colors import *
import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Let's hang!")   #Naming the window
clock = pygame.time.Clock()

class hangman:
    def __init__(self, maxFails):
        self.maxFails= self.max = maxFails
        self.greeting()
        self.createGuess()
        self.tried = False
        self.failedLetters = []
        self.win = True
        self.score = 0
        if self.max == 2:
            self.point = 750
        elif self.max == 3:
            self.point = 400
        elif self.max == 5:
            self.point = 200

    def replay(self):
        self.maxFails = self.max
        self.greeting()
        self.createGuess()
        self.tried = False
        self.failedLetters = []
        self.win = True
        if self.max == 2:
            self.point = 750
        elif self.max == 3:
            self.point = 400
        elif self.max == 5:
            self.point = 200
        self.game()

    def greeting(self):                   #this shall be replaced by the catagories input and the reading of the file that selects the word
        self.guess = self.word = input("Welcome! Enter a word! ").upper()

    def createGuess(self):
        for i in self.word:
            if i != ' ':
                self.guess = self.guess.replace(i, '_')

    def correct(self):
        guess2 = "".join(self.guess)
        if guess2 == self.word:
            return True
        else:
            return False

    def display(self):
        if self.maxFails < self.max:
            failedLetters2 = "".join(self.failedLetters)
            fld = textBox(text = failedLetters2, ypixel= 100, xpixel = 730, color = RED)
            fld.displayBlit()
        guess2 = '';                                                 #FOR LOOP GUESS INTO GUESS2 AND ADD SPACES IN BETWEEN SO WHEN PASSING ON TO GUESSD THERE WOULD BE SPACES
        for letter in self.guess:
            guess2 += str(letter) + " "
        guessD = textBox(text = guess2, ypixel= 500, color = BLACK, size= 100)
        guessD.fitToScreen()
        guessD.displayBlit()
        tries = "Tries remaining: " + str(self.maxFails)
        triesD = textBox(text = tries, xpixel= 0, ypixel= 0, center = False)
        triesD.displayBlit()
        self.triedD.displayBlit()

    def game(self):
        self.win = False
        finish = False
        cont = False
        self.guess = list(self.guess)
        self.guessLetter = ''
        self.triedD = textBox(text = "You've already tried that", xpixel = display_width/2, ypixel = 150, center = True, color = list(WHITE), size = 50)
        
        while self.win != True and self.maxFails != 0:
            gameDisplay.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if len(self.guessLetter) != 0 and event.type == pygame.KEYDOWN and event.key == 13:
                    cont = True
                if event.type == pygame.KEYDOWN and event.key != 13:
                    self.guessLetter = event.unicode
                    self.guessLetter = self.guessLetter.upper()
                else:
                    pass

            guessLetterD = textBox(text = self.guessLetter)
            guessLetterD.displayBlit()

            self.failed = True
            self.tried = False

            if self.triedD.color[1] < 255:   #When guessing a letter that's already guess it makes the message fade from red to white
                self.triedD.color[1] += 4
                self.triedD.color[2] += 4
        
            if cont == True:
                cont = False
                self.triedD.color = [255, 255, 255]    #When you guess another word it makes the triedD text white

                if self.guessLetter in self.failedLetters + self.guess:   #Check if the letter has already been in use
                    self.tried = True
                    self.guessLetter = ''
                    self.triedD.color = [255, 3, 3]   #Creates a red colored text when you repeat a letter
                    continue
                
                for index in range(len(self.word)):      #Gets the letter input, checks it with the word string, and then shoves it into the guess list checks if letter failed
                    if self.guessLetter == self.word[index]:
                        self.guess[index] = self.guessLetter
                        self.failed = False

                if self.failed == True:      #Put guessed letter in a list of failed letters
                    self.failedLetters.append(self.guessLetter)
                    self.maxFails -= 1
                
                self.guessLetter = ''
                self.win = self.correct()
            
            self.display()
            pygame.display.update()
            clock.tick(60)

        if self.win == True:     #Finish texts
            finishD = textBox(text = 'Congratulations you won!', ypixel = 200)
        else:
            finishD = textBox(text = "You Lose", ypixel = 200)

        continueD = textBox(text = 'Press any button to continue')

        while finish != True:   #print the finish message before continuing
            gameDisplay.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    finish = True
            
            self.display()
            finishD.displayBlit()
            continueD.displayBlit()
            pygame.display.update()
            clock.tick(60)

        self.score += self.maxFails * self.point

if __name__ == "__main__":
    game = hangman(3)
    game.game()