#from engines import berlinerengine as ce
import chess as ch
from game_config import *

class Engine:

    def __init__(self, board=ch.Board):
        self.__board=board

    def get_legal_moves(self):
        if self.__board.legal_moves.count() > 0:
            return [i.uci() for i in self.__board.legal_moves]
        else:
            return None

    def play_move(self, move:str):
       print("move: ",move)
       self.__board.push(ch.Move.from_uci(move))

    def get_fen(self):
        print(self.__board.fen())
        print(self.__board.fen().split(" ")[0])
        return self.__board.fen().split(" ")[0]

    def get_color(self):
        color = "w" if self.__board.turn == ch.WHITE else "b"
        return color

    #play human move
    # def playHumanMove(self):
    #     try:
    #         print(self.board.legal_moves)
    #         print("To undo your last move, type "undo")
    #         #get human move
    #         play = input("Your move: ")
    #         if (play=="undo"):
    #             self.board.pop()
    #             self.board.pop()
    #             self.playHumanMove()
    #             return
    #         self.board.push_san(play)
    #     except:
    #         self.playHumanMove()

    #play engine move
    """def playEngineMove(self, maxDepth, color):
        engine = ce.Berlinerengine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())"""

    @property
    def outcome(self):
        if self.__board.is_checkmate():
            return "checkmate"
        elif self.__board.is_stalemate():
            return "stalemate"
        elif self.__board.is_fivefold_repetition():
            return "fivefold_repetion"
        elif self.__board.is_fifty_moves():
            return "fifty_moves"
        elif self.__board.is_check():
            return "check"
        else:
            return None



    #start a game
    #def startGame(self):
        #get human player's color
        #color=None
        #while(color!="b" and color!="w"):
        #color = input(""Play as (type "b" or "w"): """)
        #maxDepth=None
        #choosing depth
        #while(isinstance(maxDepth, int)==False):
            #maxDepth = int(input("""Choose depth: """))
        #playing loop
        """while(self.endchecks()==False):
            if P_COLOR=="b":
                print("The engine is thinking...")
                self.playEngineMove(MAX_DEPTH, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            elif P_COLOR=="w":
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.playEngineMove(MAX_DEPTH, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #reset the board
        self.board.reset
        #start another game
        self.startGame()"""

#create an instance and start a game
"""newBoard= ch.Board()
game = Engine(newBoard)
bruh = game.startGame()"""
