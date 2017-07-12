# Chess Pieces
import numpy as np

class Piece(object):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"

	def setLocation(self, x, y):
		self.location = np.array([x,y])

	def isFriendly(self, piece):
		if self.team == piece.team:
			return True
		else:
			return False

class Pawn(Piece):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"
		self.type = 'Pawn'

	def move(self, board, new_ new_y):
		new_location = np.array([new_x, new_y])
		delta = new_location - self.locationx
		curr_index = (self.location[0] * 11) + self.location[1]
		new_index = (new_x * 11) + new_y
		if not board.spaces[new_index].isOccupied():
			if delta[0] == 0:
				if delta[1] == 1 or delta[1] == -1:
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].addPiece(self)
			elif delta[1] == 0:
				if delta[0] == 1 or delta[1] == -1:
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].addPiece(self)
			else:
				print('Move not Valid')
		elif board.spaces[new_index].isOccupied():
			if board.spaces[new_index].pieces[0].isFriendly():
				print('Move not Valid')
				break
			if delta[0] == -1:
				if delta[1] == -1 or delta[1] == 1:
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].removePiece()
					board.spaces[new_index].addPiece(self)
			elif delta[0] == 1:
				if delta[1] == -1 or delta[1] == 1:
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].removePiece()
					board.spaces[new_index].addPiece(self)
			else:
				print('Move not Valid')

class Rook(Piece):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"
		self.type = 'Rook'

	def move(self, board, new_x, nex_y):
		new_location = np.array([new_x, new_y])
		delta = new_location - self.locationx
		curr_index = (self.location[0] * 11) + self.location[1]
		new_index = (new_x * 11) + new_y
		if delta[0] == 0:


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