import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10
WINDOW_SIZE = (700,700)
BACKGROUND = (150,90,30)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (180,180,180)
YELLOW = (255,255,0)
CELL_QTY = 8
CELL_SIZE = 80
COLORS = [BLACK,GREY]
screen = pg.display.set_mode(WINDOW_SIZE)

#init and draw initial content
screen.fill(BACKGROUND)

#fnt_obj = pg.Font('assets/fonts/Arial.ttf',140)
#fnt_obj = pg.font.Font(pg.font.get_default_font(),140)
print(pg.font.get_fonts())
fnt_obj = pg.font.SysFont("verdana",140, italic=True)
text1 = fnt_obj.render("Our text 1",1,WHITE, BLACK)
text2 = fnt_obj.render("Our text 2",0,YELLOW, BLACK)

screen.blit(text1,(10,10))
screen.blit(text2,(10,180))

pg.display.update()
# or pg.display.flip()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        #other content handlers
    pg.display.update() #render of the screen, the most resourcefull process so it's better too call once
    clock.tick(FPS) #eval time intervals for all oper.systems