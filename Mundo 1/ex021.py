"""Tocar um áudio mp3"""
import pygame

pygame.init()
pygame.mixer.init()

audio_mp3 = "C:/Users/Cauan/Documents/Scripts/Exercícios/Cartoon.mp3"

pygame.mixer.music.load(audio_mp3)
pygame.mixer.music.play()
""" pygame.mixer.music.stop() """
while pygame.mixer.music.get_busy():
    pass
    
    
    
    
"""  if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            pygame.mixer.music.stop() """ 
