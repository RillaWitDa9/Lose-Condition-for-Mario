end = False
import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("EEL")  # sets the window title
screen = pygame.display.set_mode((1280, 720))  # creates game screen
screen.fill((255,150,0))
clock = pygame.time.Clock() #set up clock
dog = pygame.image.load("sheesh.jpg")
WTF = pygame.image.load("carr.jpg")


while not end:
    
   # screen.blit(Win, (0,600))
    font = pygame.font.Font(None, 65)
    text = font.render(str("You lose lmao, Martin doo doo caca brown at this game lmao"), 5, (255,255,255))
    screen.blit(text, (480, 435))
    #screen.blit(win1, (-50, 450))
    screen.blit(WTF, (700, 309))
    screen.blit(dog, (250, 130))

    pygame.display.flip()
pygame.quit()