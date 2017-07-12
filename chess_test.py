from chess_board import *
from chess_pieces import *

board = Board()

print(len(board.spaces))

print(board.spaces[22].x)
print(board.spaces[22].y)
print(board.spaces[22].isOccupied())

pawn1 = Pawn(1, 'pawn1')

board.spaces[22].addPiece(pawn1)

print(pawn1.location)

print(board.spaces[22].isOccupied())

pawn1.move(board, 3, 0)

print(board.spaces[22].isOccupied())
print(board.spaces[33].isOccupied())

