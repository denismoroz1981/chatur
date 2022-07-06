import chess as ch



board = ch.Board()
depth = 3
#list with first moves
first_moves = [i.uci() for i in board.legal_moves]

print(first_moves)

#dictionary with the second moves
second_moves = {}
for move in first_moves:
    board.push(ch.Move.from_uci(move))
    listMoves = [i.uci() for i in board.legal_moves]
    second_moves.update({move:listMoves})
    board.pop()

print(second_moves)

#dictionary with the third moves
third_moves={}
for key in second_moves:
    board.push(ch.Move.from_uci(key))
    for move in second_moves[key]:
        board.push(ch.Move.from_uci(move))
        listKey =[]
        listKey.append(key)
        listKey.append(move)
        listMoves = [i.uci() for i in board.legal_moves]
        third_moves.update({tuple(listKey):listMoves})
        board.pop()
    board.pop()

print(third_moves)

#dictionary with nex moves
for i in range(depth):
    next_moves={}
    for key in third_moves:
        listKeyPrev = [i for i in key]
        for i in listKeyPrev: board.push(ch.Move.from_uci(i))
        for move in third_moves[key]:
            board.push(ch.Move.from_uci(move))
            listKey =[]
            for i in listKeyPrev: listKey.append(i)
            listKey.append(move)
            listMoves = [i.uci() for i in board.legal_moves]
            next_moves.update({tuple(listKey):listMoves})
            board.pop()
        for i in range(len(listKeyPrev)): board.pop()
    third_moves = next_moves
print("-")
print("--------------------------------------------------------------------------------------------------------------")
print(next_moves)
for i in range(5): print('\a')