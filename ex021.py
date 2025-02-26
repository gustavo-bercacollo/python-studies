# Exercise Python #021 - Playing an MP3 File

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('assets/ex021_music.mp3')
pygame.mixer.music.play()

input("Press Enter to stop the music...")
pygame.mixer.music.stop()
