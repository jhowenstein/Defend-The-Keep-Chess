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

	def move(self):
		pass

class Pawn(Piece):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"
		self.type = 'Pawn'

	def move(self, board, new_x, new_y):
		new_location = np.array([new_x, new_y])
		delta = new_location - self.locationx
		curr_index = board_index(self.location[0], self.location[1])
		new_index = board_index(new_x, new_y)
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
				# Loop break might be necessary
			else:
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
		curr_index = board_index(self.location[0], self.location[1])
		new_index = board_index(new_x, new_y)
		if delta[0] == 0:
			if abs(delta[1]) > 1:
				if delta[1] > 0:
					for i in np.arange(1,delta[1]):
						if board.spaces[board_index(self.location[0],self.location[1] + i)].isOccupied():
							print('Move not Valid')
							# Probably will need a break here
				elif delta[1] < 0:
					for i in np.arang(-1,delta[1]):
						if board.spaces[board_index(self.location[0],self.location[1] + i)].isOccupied():
							print('Move not Valid')
							# Probably will need a break here
			if board.spaces[new_index].isOccupied():
				if board.spaces[new_index].pieces[0].isFriendly():
					Print('Move not Valid')
				else: # If the location is occupied by an enemy piece; capture it
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].removePiece()
					board.spaces[new_index].addPiece(self)
			else: # If the location is not occupied; move there
				board.spaces[curr_index].removePiece()
				board.spaces[new_index].addPiece(self)
		elif delta[1] == 0:
			if abs(delta[0]) > 1:
				if delta[0] > 0: # Was the move in positive direction?
					for i in np.arange(1,delta[0]):
						if board.spaces[board_index(self.location[0] + i,self.location[1])].isOccupied():
							print('Move not Valid')
							# Probably will need a break here
				elif delta[0] < 0:
					for i in np.arang(-1,delta[0]):
						if board.spaces[board_index(self.location[0] + i,self.location[1])].isOccupied():
							print('Move not Valid')
							# Probably will need a break here
			if board.spaces[new_index].isOccupied():
				if board.spaces[new_index].pieces[0].isFriendly():
					Print('Move not Valid')
				else: # If the location is occupied by an enemy piece; capture it
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].removePiece()
					board.spaces[new_index].addPiece(self)
			else: # If the location is not occupied; move there
				board.spaces[curr_index].removePiece()
				board.spaces[new_index].addPiece(self)

class Bishop(Piece):
	pass

class Knight(Piece):
	pass

class King(Piece):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([99,99]) # Place holder location, will also be consider "off board"
		self.type = 'King'

	def move(self, board, new_x, new_y):
		new_location = np.array([new_x, new_y])
		delta = new_location - self.locationx
		curr_index = board_index(self.location[0], self.location[1])
		new_index = board_index(new_x, new_y)
		if delta[0] == 0 and delta[1] == 0:
			print('Select a new space to move this piece')
			# Break loop
		if abs(delta[0]) <= 1 and abs(delta[1]) <= 1:
			if board.spaces[new_index].isOccupied():
				if board.spaces[new_index]isFriendly():
					print('Move not Valid')
					# Break loop
				else:
					board.spaces[curr_index].removePiece()
					board.spaces[new_index].removePiece()
					board.spaces[new_index].addPiece(self)
			else:
				board.spaces[curr_index].removePiece()
				board.spaces[new_index].addPiece(self)
		else:
			print('Move not Valid')


class Queen(Piece):
	pass

class Keep(Piece):
	def __init__(self, team, name):
		self.team = team
		self.name = name
		self.location = np.array([100,100]) # Special Place Holder for Keep. If location == 99,99 then game is over
		self.type = 'Keep'

	def GameOver(self):
		if self.location[0] == 99 and self.location[1] == 99:
			if self.team = 0:
				print('Game Over. Black Team Wins!')
			elif self.team = 1:
				print('Game Over. White Team Wins!')

	def move(self):
		print('Cannot move keep. Select another piece to move.')



