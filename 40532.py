import pygame,random,time,os,np
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World!')
game_over=False
flwImg=pygame.image.load('1234.png')
fstartx=100
fstarty=0
mapFile = open('7.txt','r')
flines=mapFile.readlines()
rows=len(flines)
content=np.zeros((rows,rows))
print(content)
row=0
spaceRect=((0,0,0,0))
DECSURF = pygame.Surface((400,300))
x=0
y=0
TILEWIDTH=50
TILEFLOORHEIGHT =50
TILEHEIGHT=50

for line in flines:
    col=0
    line=line.strip()
    nline=line
    for i in nline:
        content[row,col] =str(nline[col])
        col=col+1
    row=row+1
print(content)

IMAGEDICT = {'wall':pygame.image.load('w3.png'),
             'ifloor':pygame.image.load('p3.png'),
             'star':pygame.image.load('star2.png')
             }
TILEMAPPING = {'1':IMAGEDICT['wall'],
               '0':IMAGEDICT['ifloor'],
               '3':IMAGEDICT['star']}
baseTile=TILEMAPPING['1']
for y in range(len(content)):
    print("y=",y)
    for x in range(len(content[y])):
        print(x)
        spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEHEIGHT,TILEWIDTH))
        print("contentxy",content[x][y])
# time.sleep(1)
        if str(int(content[y][x])) in TILEMAPPING:
            print("contentxy",content[x][y])
            baseTile = TILEMAPPING[str(int(content[y][x]))]
# elif mapObj[x][y] in OUTSIDEDECOMAPPING:
# baseTile = TILEMAPPING[' '] """
            time.sleep(0.1)
# First draw the base ground/wall tile.
            DISPLAYSURF.blit(baseTile, spaceRect)
            pygame.display.update()

x=2
y=0

while (not game_over): #main game Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over=True
    time.sleep(0.3)
    keys = pygame.key.get_pressed()
    oldx=x
    oldy=y
    newx=x
    newy=y
    
    if keys [pygame.K_DOWN]:
        fstarty = fstarty+50
        newy=y+1
        print(str(int(content[newy,x])))
        if(str(int(content[newy,x])))== '0':
            if fstarty >=200:
                fstarty =200
            y=y+1
        else:
            fstarty = fstarty-50
    elif keys [pygame.K_UP]:
        fstarty = fstarty-50
        newy=y-1
        print(str(int(content[newy,x])))
        if print(str(int(content[newy,x])))=='0':
            if fstarty <=0:
                fstarty =0
            y=y-1
        else:
            fstarty = fstarty+50
    if keys [pygame.K_LEFT] or keys[K_a]:
        fstartx = fstartx-50
        newx=x-1
        print(str(int(content[y,newx])))
        if(str(int(content[y,newx])))== '0':
            if fstartx <=0:
                fstartx =0
            x=x-1
        else:
            fstartx = fstartx+50
    elif keys [pygame.K_RIGHT] or keys[K_d]:
        fstartx = fstartx+50
        newx=x+1
        print(str(int(content[y,newx])))
        if(str(int(content[y,newx])))== '0':
            if fstartx >=200:
                fstartx =200
            x=x+1
        else:
            fstartx = fstartx-50
    newx=x
    newy=y
    #oldx=x
    #oldy=y
    time.sleep(0.3)
    #DISPLAYSURF.fill((255,255,255))
    #DISPLAYSURF.fill((0,0,0))
    print('x=',x,'y=',y)
    
    DISPLAYSURF.blit(flwImg,(fstartx,fstarty))
    pygame.display.update()
    if str(int(content[oldy][oldx])) in TILEMAPPING:
        print("contentoldxy",content[oldx][oldy])
        baseTile = TILEMAPPING[str(int(content[oldy][oldx]))]
        #    elif map0bj[x][y] in OUTSIDEDECOMAPPING:
        #        baseTile = TILEMAPPING['  ']     """
        time.sleep(0.1)
        spaceRect = pygame.Rect((oldx * TILEWIDTH, oldy * TILEFLOORHEIGHT, TILEHEIGHT, TILEWIDTH))
        #Redraw the front ground/wall tile.
    DISPLAYSURF.blit(baseTile, spaceRect)
    
mapFile.close()
pygame.quit()

