
class Board(object):
	def __init__(self):
		self.spaces = []
		for i in range(11):
			for j in range(11):
				self.spaces.append(Space(i,j))

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
		BLACK_KEEP = Keep(0, 'Black Keep')

		# Initialize White Team Locations
		self.spaces[79].addPiece(WP1)
		self.spaces[80].addPiece(WP2)
		self.spaces[81].addPiece(WP3)
		self.spaces[82].addPiece(WP4)
		self.spaces[83].addPiece(WP5)
		self.spaces[84].addPiece(WP6)
		self.spaces[85].addPiece(WP7)
		self.spaces[93].addPiece(WP8)
		self.spaces[91].addPiece(WB1)
		self.spaces[92].addPiece(WKn1)
		self.spaces[94].addPiece(WKn2)
		self.spaces[95].addPiece(WB2)
		self.spaces[102].addPiece(WR1)
		self.spaces[103].addPiece(WQ)
		self.spaces[104].addPiece(WHITE_KEEP)
		self.spaces[105].addPiece(WK)
		self.spaces[106].addPiece(WR2)

		# Initialize Black Team Locations
		self.spaces[35].addPiece(BP1)
		self.spaces[36].addPiece(BP2)
		self.spaces[37].addPiece(BP3)
		self.spaces[38].addPiece(BP4)
		self.spaces[39].addPiece(BP5)
		self.spaces[40].addPiece(BP6)
		self.spaces[41].addPiece(BP7)
		self.spaces[27].addPiece(BP8)
		self.spaces[25].addPiece(BB1)
		self.spaces[26].addPiece(BKn1)
		self.spaces[28].addPiece(BKn2)
		self.spaces[29].addPiece(BB2)
		self.spaces[14].addPiece(BR1)
		self.spaces[15].addPiece(BK)
		self.spaces[16].addPiece(BLACK_KEEP)
		self.spaces[17].addPiece(BQ)
		self.spaces[18].addPiece(BR2)

class Space(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.pieces = []

	def addPiece(self, piece):
		if self.isOccupied():
			print('Error! A piece is already at this location')
			return len(self.pieces)
		else:
			self.pieces.append(piece)
			piece.setLocation(self.x, self.y)

	def removePiece(self):
		if self.isOccupied():
			self.pieces[0].setLocation(99,99)
			self.pieces = []
		else:
			print('Error! No piece to remove.')

	def isOccupied(self):
		if len(self.pieces) == 1:
			return True
		elif len(self.pieces) == 0:
			return False
		else:
			print('Error. More than one piece at location' + self.x + ', ' + self.y)
			return len(self.pieces)
