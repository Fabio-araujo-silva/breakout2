import pygame
from pygame.locals import *
from sys import exit

#inicializa o pygame
pygame.init()

#muda o nome da janela do jogo
pygame.display.set_caption('breakout2')

#seta o tamano da tela
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

#loop principal do jogo
while True:
    for event in pygame.event.get():
        
        #configura botao de saída
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        pygame.draw.rect(tela, ())
        #faz o jogo sempre atualizar
        pygame.display.update()