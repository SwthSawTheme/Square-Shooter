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

def personagem(x:int,y:int):
    rect_red = pygame.draw.rect(tela,VERMELHO,(x,y,50,50))
    return rect_red

def posicaoAleatoria():
    x = random.randint(100,1200)
    y = random.randint(100,700)
    return (x,y)


def game():
    x_player = 800
    y_player = 200
    pos = posicaoAleatoria()
    
    while True:
        tela.fill(PRETO)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT()
                exit()
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            x_player -= 10
        if keys[K_d]:
            x_player += 10
        if keys[K_w]:
            y_player -= 10
        if keys[K_s]:
            y_player += 10
        
        personagem(x_player,y_player)
        pygame.display.update()
        FPS.tick(60)
game()