"""
this is our main file, it will be responsible for handling user input and displaying the current GameState object. 
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSTION = 8
SQ_SIZE = HEIGHT // DIMENSTION
MAX_FPS = 15
IMAGES = {}

"""
Initiliaze a global dictionary of images. This will be called exactly once in the main
"""

def loadImages():
    pieces = ["wp","wR","wN","wB","wK","wQ",'bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE,SQ_SIZE))

    #Note : We can access an images by saying 'IMAGES["wp"]'
        
"""
The main driver for our code. This will handle the user input and updating the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()# only done once, before the while loop
    running  = True
    sqSelected  = () #no square is selected, keep track of the last click of the user
    playerClicks = [] #keeps track of the player clicks (tow tuples: (6,4), (4,4))
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #x,y mouse location
                col = location[0]// SQ_SIZE
                row = location[1]// SQ_SIZE
                if sqSelected == (row,col): #the user selcted the same square again
                    sqSelected = () #deslect
                    playerClicks = []
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2: #after the 2nd click, then we tell the engine to make a move
                    print(playerClicks[0][1])
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # reset user clicks
                    playerClicks = []
                    break

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""
Responsible for all the graphics within a current game state
"""

def drawGameState(screen, gs):
    drawBoard(screen) #draw the squares in the board
    drawPieces(screen, gs.board) #draw pieces on top of the ose squares


"""
Draw the squares on the board
"""

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSTION):
        for c in range(DIMENSTION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the pieces on the board using the curremt GameState.board
"""


def drawPieces(screen, board):
    for r in range(DIMENSTION):
        for c in range(DIMENSTION):
            piece = board[r][c]
            if piece != "  ":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            



main()