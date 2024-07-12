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
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "  "
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # log the move so we can undo it if needed
        self.whiteMove = not self.whiteMove
        

class Move():
    # maps keys to values
    # key : value
    rankToRows = {"1":7,"2":6,"3":5,"4":4,
                  "5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v: k for k,v in rankToRows.items()} # reverse the dictionary mapping
    filesToCols = {"h":7,"g":6,"f":5,"e":4,
                  "d":3,"c":2,"b":1,"a":0}
    colsToFiles = {v: k for k,v in filesToCols.items()} # reverse the dictionary mapping



    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow] [self.startCol]
        self.piecedCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        # make this real chess notation (eg: cross "X" for Capturing, "0-0-0" for long castling ...etc)
        return self.getRankFiles(self.startRow, self.startRow) + self.getRankFiles(self.endRow, self.endCol)

    def getRankFiles(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]