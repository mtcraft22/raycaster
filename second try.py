import pygame
import math
import threading
pygame.init()
Pantalla = pygame.display.set_mode((1200, 800))
relog = pygame.time.Clock()
juego = True
capamapa = pygame.surface.Surface((400, 400))
_mapa = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"] ,
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", ".", ".", "#", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", ".", "#", ".", "#", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", "#", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", ".", ".", "#", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", "#", "#", "#", ".", "#", "#", "#", ".", ".", ".", ".", "#", "#", "#", "#", "#", "#", "#", "#"] ,
    ["#", "#", "#", "#", ".", "#", "#", "#", ".", ".", ".", ".", "#", "#", "#", "#", "#", "#", "#", "#"] ,
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", ".", ".", "#", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", ".", "#", ".", "#", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", "#", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", ".", ".", "#", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#"] ,
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ".", "#", ".", ".", ".", "#"] ,
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"] ,
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
        self.x = 100
        self.y = 20
        self.angle = 180
        self.fov = 60
        self.sprite = pygame.draw.circle(Pantalla, (255, 0, 0), (self.x, self.y), 2)
        

    def reder(self):
        self.sprite = pygame.draw.circle(Pantalla, (255, 0, 0), (self.x, self.y), 2)


m = Minimapa(_mapa)
p = Player()



def raycaster():
    pygame.draw.rect(Pantalla,(50,50,50),(0,0,1200,400))
    pygame.draw.rect(Pantalla,(100,100,100),(0,400,1200,400))
    step=p.fov/1200
    angulo=p.fov/2-(p.fov)
    for i in range(1200):
        angulo +=step
        distancia=1
        if angulo <p.fov:
            while capamapa.get_at((int(p.x+math.sin((angulo+p.angle)*math.pi/180)*distancia),int(p.y-math.cos((angulo+p.angle)*math.pi/180)*distancia)))[1]!=0 and distancia<255:
                #pygame.draw.line(Pantalla,(0,255,0),(p.x,p.y),(p.x+math.sin((angulo+p.angle)*math.pi/180)*distancia,p.y-math.cos((angulo+p.angle)*math.pi/180)*distancia),3)
                distancia +=1
        
        color = (255-distancia)
        pygame.draw.rect(Pantalla,(color,color,color),(i,200,1,600-(distancia)))
        
        
while juego:
    relog.tick(60)
    Pantalla.fill((0, 0, 0))
    
    m.rederizar()
   
    #Pantalla.blit(capamapa, (0, 0))
    raycaster()
    #p.reder()  
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False

    if pygame.key.get_pressed()[pygame.K_s]:
        p.distacia = 1
        p.x += -int(math.sin(p.angle * math.pi/180)*5)
        p.y += int(math.cos(p.angle * math.pi / 180)*5)


    elif pygame.key.get_pressed()[pygame.K_w]:
        p.distacia = 1
        p.x -= -int(math.sin(p.angle * math.pi / 180)*5)
        p.y -= int(math.cos(p.angle * math.pi / 180)*5)


    elif pygame.key.get_pressed()[pygame.K_d]:
        p.angle += 5
        p.distacia = 1


    elif pygame.key.get_pressed()[pygame.K_a]:
        p.distacia = 1
        p.angle -= 5


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
