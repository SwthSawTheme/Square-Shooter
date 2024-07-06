import pygame
import os
import time
import random
from sys import exit
from pygame.locals import *

pygame.init()

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

largura = 1280
altura = 720

tela = pygame.display.set_mode((largura,altura))
FPS = pygame.time.Clock()
pygame.display.set_caption("Square Shooter")

def game():
    
    while True:
        tela.fill(PRETO)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()
        
                
        pygame.display.update()
        FPS.tick(60)
game()