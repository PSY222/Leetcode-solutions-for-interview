from collections import Counter, defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        second_cond = defaultdict(list)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    second_cond[j].append(board[i][j])
        
        boxes = []
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                boxes.append(square)
        
        return False if False in [self.condition(boxes),self.condition(board),self.condition(second_cond.values())] else True

        
    def condition(self,arr):
        for i in arr:
            for val, cnts in Counter(i).items():
                if val != '.' and cnts>=2:
                    return False
        return True
            