import pygame as pg

from game_config import *
from chess_items import *

clock = pg.time.Clock()

screen = pg.display.set_mode(WINDOW_SIZE)

#init and draw initial content
screen.fill(BACKGROUND)

#chessboard = Chessboard(screen, 4, 100)
chessboard = Chessboard(screen)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            chessboard.btn_down(event.button,event.pos)
        if event.type == pg.MOUSEBUTTONUP:
            chessboard.btn_up(event.button, event.pos)
        if event.type == pg.MOUSEMOTION:
            chessboard.drag(event.pos)
        if event.type == pg.KEYDOWN:
            chessboard.key_down(event)
        if event.type == pg.KEYUP:
            chessboard.key_up(event)

        #other content handlers
    # pg.display.update() #render of the screen, the most resourcefull process so it's better too call once
    # clock.tick(FPS) #eval time intervals for all oper.systems