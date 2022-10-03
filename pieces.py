import pygame as pg
from game_config import *

class Piece(pg.sprite.Sprite):
    def __init__(self, cell_size: int, color:str, field_name:str,
        file_posfix:str, is_pawn:bool = False, outcome:str = False):
        super().__init__()
        picture = pg.image.load(PIECE_PATH + color + file_posfix).convert_alpha()
        self.image = pg.transform.scale(picture, (cell_size, cell_size))
        self.rect = self.image.get_rect() # -> pg.Rect(0,0,70,70)
        self.color = color
        self.field_name = field_name
        self.is_pawn = is_pawn
        self.outcome = outcome


    def move_to_cell(self, cell): #will use it to draw rival's move

        self.rect = cell.rect.copy()
        self.field_name = cell.field_name



class King(Piece):
    def __init__(self, cell_size:int, color:str,field:str,outcome:str=None):
        img = '_king.png'
        if outcome == "check": img = '_king_check.png'
        if outcome == "checkmate": img = '_king_mate.png'
        super().__init__(cell_size, color, field, img)

class Queen(Piece):
    def __init__(self, cell_size:int, color:str,field:str):
        super().__init__(cell_size, color, field,'_queen.png')

class Rook(Piece):
    def __init__(self, cell_size:int, color:str,field:str):
        super().__init__(cell_size, color, field,'_rook.png')

class Bishop(Piece):
    def __init__(self, cell_size:int, color:str,field:str):
        super().__init__(cell_size, color, field,'_bishop.png')

class Knight(Piece):
    def __init__(self, cell_size:int, color:str,field:str):
        super().__init__(cell_size, color, field,'_knight.png')

class Pawn(Piece):
    def __init__(self, cell_size:int, color:str,field:str):
        super().__init__(cell_size, color, field,'_pawn.png', True)
