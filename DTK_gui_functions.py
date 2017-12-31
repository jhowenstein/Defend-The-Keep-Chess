# Defend The Keep Chess GUI Functions
import pygame, sys, math
from pygame.locals import *

def drawBoard(DISPLAYSURF, BOARDWIDTH, SQUARE_SIZE, XMARGIN, YMARGIN, color1, color2):
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
			i += 1

def determineSpace(mousex, mousey, XMARGIN, YMARGIN, SQUARE_SIZE):
	row = math.ceil((mousey - YMARGIN) / SQUARE_SIZE)
	col = math.ceil((mousex - XMARGIN) / SQUARE_SIZE)
	print(row,',',col)
	return row, col

def highlightSpace(DISPLAYSURF, XMARGIN, YMARGIN, HIGHLIGHT_COLOR, row, col):
	left = XMARGIN + ((col - 1) * SQUARE_SIZE)
	top = YMARGIN + ((row - 1) * SQUARE_SIZE)
	pygame.draw.rect(DISPLAYSURF, HIGHLIGHT_COLOR, (left, top, SQUARE_SIZE, SQUARE_SIZE))

def unHighlight(DISPLAYSURF, XMARGIN, YMARGIN, board, row, col):
	left = XMARGIN + ((col - 1) * SQUARE_SIZE)
	top = YMARGIN + ((row - 1) * SQUARE_SIZE)
	space_index = board_index(row, col)
	original_color = board.spaces[space_index].color
	pygame.draw.rect(DISPLAYSURF, original_color, (left, top, SQUARE_SIZE, SQUARE_SIZE))
