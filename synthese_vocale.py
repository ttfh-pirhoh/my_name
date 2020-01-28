from soundsystem import *

initTTS()

selectVoice("german-man")
#selectVoice("german-woman")
#selectVoice("english-man")
#selectVoice("english-woman")
#selectVoice("french-woman")
#selectVoice("french-man")
#selectVoice("italian-woman")

text = "Danke dass du mir eine Sprache gibst. Viel Spass beim Programmieren" 
#text = "Thank you to give me a voice. Enjoy programming" 
#text = "Merci pour me donner une voix. Profitez de la programmation"
#text = "Grazie che tu mi dia una lingua. Godere della programmazione"
voice = generateVoice(text)
openSoundPlayer(voice)
play()