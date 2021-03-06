import berlinerengine as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    #play human move
    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")
            #get human move
            play = input("Your move: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #play engine move
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    #checks on game end
    def endchecks(self):
        endcheck = False
        if self.board.is_checkmate():
            print("Checkmate!")
            endcheck = True
        elif self.board.is_stalemate():
            print("Stalemate -> DRAW")
            endcheck = True
        elif self.board.is_fivefold_repetition():
            print("Fivefold repetition -> DRAW")
            endcheck = True
        elif self.board.is_fifty_moves():
            print("Fifty moves -> DRAW")
            endcheck = True
        elif self.board.is_check():
            print("Check!")
            endcheck = True
        return endcheck

    #start a game
    def startGame(self):
        #get human player's color
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        maxDepth=None
        #choosing depth
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Choose depth: """))
        #playing loop
        while(self.endchecks()==False):
            if color=="b":
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            elif color=="w":
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #reset the board
        self.board.reset
        #start another game
        self.startGame()

#create an instance and start a game
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()