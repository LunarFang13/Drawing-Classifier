import pygame as pg
import random
import drawingtoarray

def init():
    global screen
    global prompt
    f = open("labels.txt","r")
    labels = f.readlines()
    f.close()
    prompt = random.choice(labels).capitalize().replace('_', ' ')
    pg.init()
    screen = pg.display.set_mode((800,800))
    bgcolor = (255,255,255)
    screen.fill(bgcolor)
    pg.font.init()
    my_font = pg.font.SysFont('Comic Sans MS', 25)
    text_surface = my_font.render(prompt[0:len(prompt)-1], False, (0,0,0))
    screen.blit(text_surface, (350,10))
    pg.draw.rect(screen, (0,0,0), pg.Rect(50, 50, 700, 700))
    mainloop()
 
 
drawing = False
last_pos = None
w = 10
drawcolor = (255, 255, 255)

 
 
def draw(event):
    global drawing, last_pos, w
    if event.type == pg.MOUSEMOTION:
        if (drawing):
            mouse_position = pg.mouse.get_pos()
            if last_pos is not None:
                pg.draw.line(screen, drawcolor, last_pos, mouse_position, w)
            last_pos = mouse_position
    elif event.type == pg.MOUSEBUTTONUP:
        mouse_position = (0, 0)
        drawing = False
        last_pos = None
    elif event.type == pg.MOUSEBUTTONDOWN:
        drawing = True
 
 
def mainloop():
    global screen
 
    loop = 1
    while loop:
        # checks every user interaction in this list
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    pg.image.save(screen, "image.png")
                    drawingtoarray.dta()
                elif event.key == pg.K_r:
                    init()
            draw(event)
        pg.display.flip()
    pg.quit()
 
 
init()