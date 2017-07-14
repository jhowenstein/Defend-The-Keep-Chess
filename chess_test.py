
from chess_board import *
from chess_pieces import *

board = Board()

# Initialize Piece Locations
# Initialize White team (Team = 0)
WP1 = Pawn(0, 'WP1')
WP2 = Pawn(0, 'WP2')
WP3 = Pawn(0, 'WP3')
WP4 = Pawn(0, 'WP4')
WP5 = Pawn(0, 'WP5')
WP6 = Pawn(0, 'WP6')
WP7 = Pawn(0, 'WP7')
WP8 = Pawn(0, 'WP8')
WB1 = Bishop(0, 'WB1')
WB2 = Bishop(0, 'WB2')
WKn1 = Knight(0, 'WKn1')
WKn2 = Knight(0, 'WKn2')
WR1 = Rook(0, 'WR1')
WR2 = Rook(0, 'WR2')
WQ = Queen(0, 'WQ')
WK = King(0, 'WK')
WHITE_KEEP = Keep(0, 'White Keep')

# Initialize Black Team (Team = 1)
BP1 = Pawn(1, 'BP1')
BP2 = Pawn(1, 'P2')
BP3 = Pawn(1, 'BP3')
BP4 = Pawn(1, 'BP4')
BP5 = Pawn(1, 'BP5')
BP6 = Pawn(1, 'BP6')
BP7 = Pawn(1, 'BP7')
BP8 = Pawn(1, 'BP8')
BB1 = Bishop(1, 'BB1')
BB2 = Bishop(1, 'BB2')
BKn1 = Knight(1, 'BKn1')
BKn2 = Knight(1, 'BKn2')
BR1 = Rook(1, 'BR1')
BR2 = Rook(1, 'BR2')
BQ = Queen(1, 'BQ')
BK = King(1, 'BK')
BLACK_KEEP = Keep(1, 'Black Keep')

# Initialize White Team Locations
board.spaces[79].addPiece(WP1)
board.spaces[80].addPiece(WP2)
board.spaces[81].addPiece(WP3)
board.spaces[82].addPiece(WP4)
board.spaces[83].addPiece(WP5)
board.spaces[84].addPiece(WP6)
board.spaces[85].addPiece(WP7)
board.spaces[93].addPiece(WP8)
board.spaces[91].addPiece(WB1)
board.spaces[92].addPiece(WKn1)
board.spaces[94].addPiece(WKn2)
board.spaces[95].addPiece(WB2)
board.spaces[102].addPiece(WR1)
board.spaces[103].addPiece(WQ)
board.spaces[104].addPiece(WHITE_KEEP)
board.spaces[105].addPiece(WK)
board.spaces[106].addPiece(WR2)

# Initialize Black Team Locations
board.spaces[35].addPiece(BP1)
board.spaces[36].addPiece(BP2)
board.spaces[37].addPiece(BP3)
board.spaces[38].addPiece(BP4)
board.spaces[39].addPiece(BP5)
board.spaces[40].addPiece(BP6)
board.spaces[41].addPiece(BP7)
board.spaces[27].addPiece(BP8)
board.spaces[25].addPiece(BB1)
board.spaces[26].addPiece(BKn1)
board.spaces[28].addPiece(BKn2)
board.spaces[29].addPiece(BB2)
board.spaces[14].addPiece(BR1)
board.spaces[15].addPiece(BK)
board.spaces[16].addPiece(BLACK_KEEP)
board.spaces[17].addPiece(BQ)
board.spaces[18].addPiece(BR2)

TURN = 0 # Determine who has first move (White = 0, Black = 1)

while WHITE_KEEP.status and BLACK_KEEP.status:
	SELECT = 1

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
		print(target_col)
		if row < 0 or row > 10:
			print('Error. Invalid Location')
		elif col < 0 or col > 10:
			print('Error. Invalid Location')
		else:
			MOVE = board.spaces[board_index(row,col)].pieces[0].move(board, target_row, target_col)
			if MOVE == 0:
				print('Move Sucessful')
				if TURN == 0:
					TURN = 1
				elif TURN == 1:
					TURN = 0
