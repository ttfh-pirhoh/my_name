from os import chdir
from speechrecognition import parler
from interagir import robotResponse
import audio
from response_audio import textToSpeech
import pydub
import pygame
from lecture import lecture
path="g:/python/smart_robot_test"
language="fr"
chdir(path)
import speechrecognition
import interagir
text=parler()
response=robotResponse(text)
print(response)
textToSpeech(response)
#conversion
pygame.init()
sound = pydub.AudioSegment.from_mp3("g:/python/smart_robot_test/response.mp3")
sound.export(path+"/response.wav", format="wav")
pygame.mixer.music.set_volume(0.99)

lecture("g:/python/smart_robot_test/response.wav")
