import pygame, sys
import random
from math import sin, cos, pi, atan

from pygame.locals import *


#podstawy

rozmiar = 800
bok = 30


pygame.init()
plansza = pygame.display.set_mode((rozmiar, rozmiar))
pygame.display.set_caption('Pendulum')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAD_GREEN = (129, 187, 129)
GRAY = (200, 200, 200)
LIGHT_GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (176, 224, 230)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
PINK = (255, 105, 180)
ORANGE = (255, 140, 0)


FPS = 100
fpsClock = pygame.time.Clock()



class Mass:
    def __init__(self, x0, y0, L, alpha):
        self.x0 = x0
        self.y0 = y0
        self.L = L
        self.alpha = alpha
        self.w = 0

    def move(self):
        E = g * sin(self.alpha) / self.L
        self.w += E * dt
        dalpha = self.w * dt + 0.5 * E * dt ** 2
        self.alpha += dalpha

    def setting(self, tg):
        self.alpha = atan(tg)
        self.w = 0

    def show(self):
        x = self.x0 + self.L * sin(self.alpha)
        y = self.y0 + self.L * cos(self.alpha)
        pygame.draw.line(plansza, BROWN, (self.x0, self.y0), (x, y), 3)
        pygame.draw.circle(plansza, BLACK, (x, y), 10)
        


#zainicjowanie wahadla
m1 = Mass(rozmiar/2, 100, 200, pi/3)


#potrzebne zmienne
g = -9.81
dt = 0.1

var = False


#petla glowna
while True:
    #wyswietlanie
    plansza.fill(WHITE)
    m1.show()

    #manipulowanie katem
    if var == False:
        m1.move()
    else:
        x, y = pygame.mouse.get_pos()
        if y - m1.y0 != 0:
            tg = (x - m1.x0) / (y - m1.y0)
            m1.setting(tg)

    #obsluga zdarzen
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            var = True
        if event.type == pygame.MOUSEBUTTONUP:
            var = False
          
                

    pygame.display.update()
    fpsClock.tick(FPS)