import pygame
pygame.init()
pygame.mixer.music.load('testmp3.wav')
pygame.mixer.music.play()
pygame.event.wait()