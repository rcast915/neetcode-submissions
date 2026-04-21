from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        cube = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                
                elif (curr in row[i]) or (curr in col[j]) or (curr in cube[(i//3, j//3)]):
                    return False
                

                row[i].add(curr)
                col[j].add(curr)
                cube[(i//3, j//3)].add(curr)
                
        return True
                
        