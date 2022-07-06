import chess as ch
import random as rd


class Engine:

    def __init__(self, board, maxDepth, color):
        self.board = board
        self.color = color
        self.maxDepth = maxDepth
        self.contra_color = ch.WHITE if self.color == ch.BLACK else ch.BLACK



    def getBestMove(self):
        return self.engine()

    def evalFunct(self):
        scores = {ch.PAWN:1,
                  ch.KNIGHT:3.2,
                  ch.BISHOP:3.33,
                  ch.ROOK:5.1,
                  ch.QUEEN:8.8
                  }
        compt = 0
        # Sums up the material values
        for i in range(64):
            compt += scores[ch.SQUARES[i]] * -1 if self.board.color_at(ch.SQUARES[i]) != self.color else 1
        compt += self.openning()+self.endchecks() + 0.001 * rd.random()
        return compt

    def endchecks(self):

            if self.board.outcome() == None: return 0
            #check on mate
            if self.board.outcome()=="checkmate":
                return -1000 if (self.board.turn == self.color) else -1000
            #check on the other ends
            else:
                if (self.board.turn == self.color):
                    return 1000 if self.board.has_insufficient_material(self.color) else -500
                else:
                    return -1000 if self.board.has_insufficient_material(self.contra_color) else -500


    # to make the engine developp in the first moves
    def openning(self):
        if (self.board.fullmove_number < 10):
            if (self.board.turn == self.color):
                return 1 / 30 * self.board.legal_moves.count()
            else:
                return -1 / 30 * self.board.legal_moves.count()
        else:
            return 0

#    engine
    def engine(self):
        # list with first moves
        first_moves = [i.uci() for i in self.board.legal_moves]
        scores = {}
        #print(first_moves)

        # dictionary with the second moves
        second_moves = {}
        for move in first_moves:
            scores.update({move:[]})
            self.board.push(ch.Move.from_uci(move))
            listMoves = [i.uci() for i in self.board.legal_moves]
            second_moves.update({move: listMoves})
            self.board.pop()

        #print(second_moves)

        # dictionary with the third moves
        third_moves = {}
        for key in second_moves:
            self.board.push(ch.Move.from_uci(key))
            for move in second_moves[key]:
                self.board.push(ch.Move.from_uci(move))
                listKey = []
                listKey.append(key)
                listKey.append(move)
                listMoves = [i.uci() for i in self.board.legal_moves]
                third_moves.update({tuple(listKey): listMoves})
                self.board.pop()
            self.board.pop()

        #print(third_moves)

        # dictionary with nex moves
        for i in range(self.maxDepth):
            next_moves = {}
            for key in third_moves:
                listKeyPrev = [i for i in key]
                for i in listKeyPrev: self.board.push(ch.Move.from_uci(i))
                for move in third_moves[key]:
                    self.board.push(ch.Move.from_uci(move))
                    listKey = []
                    for i in listKeyPrev: listKey.append(i)
                    listKey.append(move)
                    listMoves = [i.uci() for i in self.board.legal_moves]
                    next_moves.update({tuple(listKey): listMoves})
                    self.board.pop()
                for i in range(len(listKeyPrev)): self.board.pop()
            third_moves = next_moves
        print("-")
        print(
            "--------------------------------------------------------------------------------------------------------------")
        print(next_moves)
        for i in range(5): print('\a')









       # ---------------------------------------------------------------
        # reached max depth of search or no possible moves
        if (depth == self.maxDepth
                or self.board.legal_moves.count() == 0):
            return self.evalFunct()

        else:
            print("else")
            # get list of legal moves of the current position
            moveListe = list(self.board.legal_moves)

            # initialise newCandidate
            newCandidate = None
            # (uneven depth means engine's turn)
            if (depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")

            # analyse board after deeper moves
            for i in moveListe:

                # Play move i
                self.board.push(i)

                # Get value of move i (by exploring the repercussions)
                value = self.engine(newCandidate, depth + 1)

                # Basic minmax algorithm:
                # if maximizing (engine's turn)
                if (value > newCandidate and depth % 2 != 0):
                    # need to save move played by the engine
                    if (depth == 1):
                        move = i
                    newCandidate = value
                # if minimizing (human player's turn)
                elif (value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                # Alpha-beta prunning cuts:
                # (if previous move was made by the engine)
                if (candidate != None
                        and value < candidate
                        and depth % 2 == 0):
                    self.board.pop()
                    break
                # (if previous move was made by the human player)
                elif (candidate != None
                      and value > candidate
                      and depth % 2 != 0):
                    self.board.pop()
                    break

                # Undo last move
                self.board.pop()

            # Return result
            if (depth > 1):
                # eturn value of a move in the tree
                return newCandidate
            else:
                # return the move (only on first move)
                return move
