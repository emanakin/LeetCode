#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track cols, sqrs and rows
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        # ittr through board
        for i in range(9):
            for j in range(9):
                currNum = board[i][j] 
                # encounter non number
                if (currNum == "."):
                    continue
                
                # if num is found in set
                if (currNum in rows[i] or
                    currNum in cols[j] or
                    currNum in squares[((i // 3), (j // 3))]):
                    return False    
                    
                # add unfound number to corrosponding set
                rows[i].add(currNum)
                cols[j].add(currNum)
                squares[((i // 3), (j // 3))].add(currNum)
        
        return True
         
# @lc code=end
