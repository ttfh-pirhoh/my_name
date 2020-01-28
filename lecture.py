import pygame
pygame.mixer.init()
def lecture(path):
    pygame.mixer.Sound(path).play()
    i=0
    while pygame.mixer.get_busy():
        
        print(i)