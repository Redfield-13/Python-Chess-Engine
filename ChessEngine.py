"""
This class is reponsible for storing all the informations about the sate of a chess game, and also for determining the valid moves at the CurrentState, also it will keep a moves log.
"""

class GameState():
    def __init__(self):
        self.board = [
            []
        ]