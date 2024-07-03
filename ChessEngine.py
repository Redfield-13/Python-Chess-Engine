"""
This class is reponsible for storing all the informations about the sate of a chess game, and also for determining the valid moves at the CurrentState, also it will keep a moves log.
"""

class GameState():
    def __init__(self):
        # the board is an 8*8 2d list. Each element of the list has 2 charachters, 
        #The first charachter represents the color of the peice, 'w' or 'b'
        #The second charachter represnets the type of the piece: 'K', 'Q', 'R', 'B', 'N' or 'p'
        #"  " represents an empty space with no peice occupying it

        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.whiteMove = True
        self.moveLog = []
        