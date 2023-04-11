import pygame
import math
import threading
pygame.init()
Pantalla = pygame.display.set_mode((1200, 800))
relog = pygame.time.Clock()
juego = True
capamapa = pygame.surface.Surface((400, 400))
_mapa = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#", "#"],
    ["#", ".", ".", ".", ".", "#", ".", "#",".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#", "#"],
    ["#", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


class Minimapa:
    def __init__(self, mapa):
        self.mapa = mapa
        self.px = 0
        self.py = 0

    def rederizar(self):
        for y in self.mapa:
            for x in y:
                if x == "#":
                    pygame.draw.rect(capamapa, (0, 0, 255), [self.px, self.py, 20, 20])
                    self.px += 20
                elif x == ".":
                    pygame.draw.rect(capamapa, (255, 255, 255), [self.px, self.py, 20, 20])
                    self.px += 20
            self.px = 0
            self.py += 20
        self.px = 0
        self.py = 0


class Player:
    def __init__(self):
        self.x = 90
        self.y = 100
        self.angle = 0
        self.fov = 60
        self.sprite = pygame.draw.circle(Pantalla, (255, 0, 0), (self.x, self.y), 5)
        

    def reder(self):
        self.sprite = pygame.draw.circle(Pantalla, (255, 0, 0), (self.x, self.y), 5)


m = Minimapa(_mapa)
p = Player()


def raycaster():
    distacia=0
    while capamapa.get_at((int(p.x+math.sin(p.angle*math.pi/180)*distacia),int(p.y-math.cos(p.angle*math.pi/180)*distacia)))[1]!=0:
        pygame.draw.line(Pantalla,(0,255,0),(p.x,p.y),(p.x+math.sin(p.angle*math.pi/180)*distacia,p.y-math.cos(p.angle*math.pi/180)*distacia),3)
        distacia +=1
    distacia=0
    while capamapa.get_at((int(p.x+math.sin(p.angle*math.pi/180-((p.fov/2)*math.pi/180))*distacia),int(p.y-math.cos(p.angle*math.pi/180-((p.fov/2)*math.pi/180))*distacia)))[1]!=0:
        pygame.draw.line(Pantalla,(0,255,0),(p.x,p.y),(p.x+math.sin(p.angle*math.pi/180-((p.fov/2)*math.pi/180))*distacia,p.y-math.cos(p.angle*math.pi/180-((p.fov/2)*math.pi/180))*20),3)
        distacia +=1
    distacia=0
    while capamapa.get_at((int(p.x+math.sin(p.angle*math.pi/180+((p.fov/2)*math.pi/180))*distacia),int(p.y-math.cos(p.angle*math.pi/180+((p.fov/2)*math.pi/180))*distacia)))[1]!=0:
        pygame.draw.line(Pantalla,(0,255,0),(p.x,p.y),(p.x+math.sin(p.angle*math.pi/180+((p.fov/2)*math.pi/180))*distacia,p.y-math.cos(p.angle*math.pi/180+((p.fov/2)*math.pi/180))*distacia),3)
        distacia +=1
    distacia=0
    
    





while juego:
    relog.tick(60)
    Pantalla.fill((0, 0, 0))
    m.rederizar()
    Pantalla.blit(capamapa, (0, 0))
    p.reder()
    raycaster()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p.distacia = 1
                p.angle = 0
                p.y -= 5

            elif event.key == pygame.K_s:
                p.distacia = 1
                p.angle = 180
                p.y += 5

            elif event.key == pygame.K_d:
                p.distacia = 1
                p.angle = 90
                p.x += 5

            elif event.key == pygame.K_a:
                p.distacia = 1
                p.angle = 270
                p.x -= 5
    colorpisado = capamapa.get_at((p.x, p.y))





    if colorpisado[1] == 0:
        if p.angle == 0:
            p.y += 10
        elif p.angle == 90:
            p.x -= 5
        elif p.angle == 180:
            p.y -= 5
        elif p.angle == 270:
            p.x += 10

    pygame.display.update()
