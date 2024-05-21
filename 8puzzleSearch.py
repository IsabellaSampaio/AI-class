import numpy as np
from itertools import zip_longest

class Game: 
    
    def __init__(self, board):
        self.board = np.array(board)
    
    def findZero(self):
        index = np.argwhere(self.board == 0)
        if len(index) > 0:
            return index
    
    def move(self):
        index = self.findZero()
        edges = [[0,0], [0,2], [2,0], [2,2]]
        
        ble1 = sorted(self.board[0])
        ble2 = sorted(self.board[1])
        ble3 = sorted(self.board[2])
        
        list1 = [i for i, x in enumerate(ble1) if x != i]
        list2 = [i for i, x in enumerate(ble2) if x != i]
        list3 = [i for i, x in enumerate(ble3) if x != i]
        
        for i, j, k in zip_longest(list1, list2, list3, fillvalue=None):
            if i is not None and j is not None and k is not None:
                # Swap the misplaced elements
                list1[i], list2[j], list3[k] = list2[j], list3[k], list1[i]

        print(list1, list2, list3)

matrix = [
    [8, 2, 3],
    [4, 5, 6],
    [1, 7, 0]

]

game = Game(matrix)

game.findZero()

game.move()

#print(game.board)
