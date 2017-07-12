# Chess Pieces
import numpy as np

class Piece(object):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"

	def setLocation(self, x, y):
		self.location = np.array([x,y])

class Pawn(Piece):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"
		self.type = 'Pawn'

	def move(self, board, new_x, new_y):
		new_location = np.array([new_x, new_y])
		curr_index = (self.location[0] * 11) + self.location[1]
		new_index = (new_x * 11) + new_y
		if not board.spaces[new_index].isOccupied():
			if new_location[0] == self.location[0]:
				if new_location[1] == (self.location[1] + 1 or self.location[1] - 1):
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].addPiece(self)
			elif new_location[1] == self.location[1]:
				if new_location[0] == (self.location[0] + 1 or self.location[0] - 1):
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].addPiece(self)
			else:
				print('Move not Valid')
		elif board.spaces[new_index].isOccupied():
			pass

class Rook(Piece):
	pass

class Bishop(Piece):
	pass

class Knight(Piece):
	pass

class King(Piece):
	pass

class Queen(Piece):
	pass

class Keep(Piece):
	pass