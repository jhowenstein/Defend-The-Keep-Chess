# Defend The Keep Chess GUI Functions
import pygame, sys, math
from pygame.locals import *
from chess_board import *

def drawBoard(DISPLAYSURF, BOARDWIDTH, SQUARE_SIZE, XMARGIN, YMARGIN, color1, color2, board):
	i = 0;
	for SPACEy in range(BOARDWIDTH):
		for SPACEx in range(BOARDWIDTH):
			if (i / 2) == round(i / 2):
				COLOR = color1
			else:
				COLOR = color2
			left = XMARGIN + (SPACEx * SQUARE_SIZE)
			top = YMARGIN + (SPACEy * SQUARE_SIZE)
			pygame.draw.rect(DISPLAYSURF, COLOR, (left, top, SQUARE_SIZE, SQUARE_SIZE))
			if board.spaces[i].isOccupied():
				DISPLAYSURF.blit(board.spaces[i].pieces[0].img, (left, top))
			i += 1

def determineSpace(mousex, mousey, XMARGIN, YMARGIN, SQUARE_SIZE):
	row = math.ceil((mousey - YMARGIN) / SQUARE_SIZE) - 1
	col = math.ceil((mousex - XMARGIN) / SQUARE_SIZE) - 1
	print(row,',',col)
	return row, col

def highlightSpace(DISPLAYSURF, XMARGIN, YMARGIN, HIGHLIGHT_COLOR, SQUARE_SIZE, row, col):
	left = XMARGIN + (col * SQUARE_SIZE)
	top = YMARGIN + (row * SQUARE_SIZE)
	pygame.draw.rect(DISPLAYSURF, HIGHLIGHT_COLOR, (left, top, SQUARE_SIZE, SQUARE_SIZE))
	space_index = board_index(row, col)
	DISPLAYSURF.blit(board.spaces[space_index].pieces[0].img, (left, top))

def unHighlight(DISPLAYSURF, XMARGIN, YMARGIN, SQUARE_SIZE, board, row, col):
	left = XMARGIN + (col * SQUARE_SIZE)
	top = YMARGIN + (row * SQUARE_SIZE)
	space_index = board_index(row, col)
	original_color = board.spaces[space_index].color
	pygame.draw.rect(DISPLAYSURF, original_color, (left, top, SQUARE_SIZE, SQUARE_SIZE))
