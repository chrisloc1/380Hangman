from textDisplay import textBox
import pygame
import time
import random

#pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

class button:   #BUTTON PIXELS ARE NOT CENTERED
    def __init__(self,fsize,msg,x,y,w,h,ic,ac,action=None, mup = False):
        mouse = pygame.mouse.get_pos()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            if mup == True and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        buttonName = textBox([0,0,0],msg, fsize,'arial',True,(x+(w/2)),(y+(h/2)))
        buttonName.displayBlit()