import chess as ch
import random as rd


class Berlinerengine:

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
            try:
                compt += scores[ch.SQUARES[i]] * -1 if self.board.color_at(ch.SQUARES[i]) != self.color else 1
            except:
                print(ch.SQUARES[i])

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
        if self.board.legal_moves.count == 0: return None
        first_moves = [i.uci() for i in self.board.legal_moves]
        if self.board.legal_moves.count == 1: return first_moves[0]
        scores = {}
        #print(first_moves)


        # dictionary with the second moves
        second_moves = {}
        for move in first_moves:
            scores.update({move:[]})
            self.board.push(ch.Move.from_uci(move))
            if self.board.legal_moves.count() > 0:
                listMoves = [i.uci() for i in self.board.legal_moves]
                second_moves.update({move: listMoves})
                self.board.pop()
            else:
                scores[move].append(self.evalFunct())


        #print(second_moves)

        # dictionary with the third moves
        if bool(second_moves):
            third_moves = {}
            for key in second_moves:
                self.board.push(ch.Move.from_uci(key))
                for move in second_moves[key]:
                    self.board.push(ch.Move.from_uci(move))
                    if self.board.legal_moves.count() > 0:
                        listKey = []
                        listKey.append(key)
                        listKey.append(move)
                        listMoves = [i.uci() for i in self.board.legal_moves]
                        third_moves.update({tuple(listKey): listMoves})
                        self.board.pop()
                    else:
                        scores[key].append(self.evalFunct())
                self.board.pop()

        #print(third_moves)

        # dictionary with nex moves
        for depth in range(self.maxDepth):
            if not bool(third_moves): break
            next_moves = {}
            for key in third_moves:
                    listKeyPrev = [i for i in key]
                    for i in listKeyPrev: self.board.push(ch.Move.from_uci(i))
                    for move in third_moves[key]:
                        print(key)
                        print(third_moves[key])
                        self.board.push(ch.Move.from_uci(move))
                        if self.board.legal_moves.count() > 0:
                            listKey = []
                            for i in listKeyPrev: listKey.append(i)
                            listKey.append(move)
                            listMoves = [i.uci() for i in self.board.legal_moves]
                            next_moves.update({tuple(listKey): listMoves})
                            if depth == self.maxDepth-1:
                                scores[key[0]].append(self.evalFunct())
                            self.board.pop()
                        else:
                            scores[key[0]].append(self.evalFunct())
                    for i in range(len(listKeyPrev)): self.board.pop()
            third_moves = next_moves
            print("-")
            print(
                "--------------------------------------------------------------------------------------------------------------")
            #print(next_moves)

        for key in scores:
            scores[key] = max(scores[key])
        return sorted(scores,key=lambda x: scores[x])[0]
