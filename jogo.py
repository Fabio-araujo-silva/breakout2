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

#seta posição inicial do bloco
x=height/2
y=0
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

#loop principal do jogo
while True:

    #framerate
    clock.tick(30)
    #"limpa tela"
    screen.fill((0,0,0))

    for event in pygame.event.get():
        
        #configura botao de saída
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #adiciona bloco branco
        pygame.draw.rect(screen, (255,255,255),(x,y,40,40))
        if y>=height:
            y=0
        y=y+10

        #faz o jogo sempre atualizar
        pygame.display.update()