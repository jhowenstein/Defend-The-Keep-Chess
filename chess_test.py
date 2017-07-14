
from chess_board import *
from chess_pieces import *

board = Board()

SELECT = 1
TURN = 0

while SELECT == 1:
	print('Player:',TURN + 1,'Select a Piece (row,column)')
	s = input()
	row,col = s.split(',')
	row = int(row)
	col = int(col)
	if row < 0 or row > 10:
		print('Error. Invalid Location')
	elif col < 0 or col > 10:
		print('Error. Invalid Location')
	elif not board.spaces[board_index(row,col)].isOccupied():
		print('Error. No piece at this location')
	elif not board.spaces[board_index(row,col)].pieces[0].team == TURN:
		print('Error. This piece is on the other team')
	elif board.spaces[board_index(row,col)].pieces[0].type == 'Keep':
		print('Error. Cannot Move Keep')
	else:
		SELECT = 0


print('Selection Good')
print(board.spaces[board_index(row,col)].pieces[0].name)

MOVE = 1

while MOVE == 1:
	print('Player',TURN + 1,'Select Location to Move Piece')
	s = input()
	target_row,target_col = s.split(',')
	target_row = int(target_row)
	target_col = int(target_col)
	if row < 0 or row > 10:
		print('Error. Invalid Location')
	elif col < 0 or col > 10:
		print('Error. Invalid Location')
	else:
		MOVE = board.spaces[board_index(row,col)].pieces[0].move(board, target_row,target_col)
