'''
Faça um programa em Python que abra e reproduza o áudio
de um arquivo MP3.

Make a Python program that opens and plays the audio
an MP3 file.
'''
from pygame import mixer
mixer.init()
mixer.music.load('ex021.ogg')
mixer.music.play()
input('CURTE O SOM!')