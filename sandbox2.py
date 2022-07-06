import chess as ch

board = ch.Board()

print(board.legal_moves)

legal_moves = [i.uci() for i in board.legal_moves]
print(legal_moves)
