# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
import pygame
pygame.init()
def textToSpeech(mytext):
    # Language we want to use 
    myobj = gTTS(text=mytext, lang="fr") 
    myobj.save("g:/python/smart_robot_test/response.mp3") 
    print("fin de la sauvegarde en mp3")
