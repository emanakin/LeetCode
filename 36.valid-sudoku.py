#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # store the validations
        
        # validate rows
        
        # validate cols
        
        # validate 3x3 sections
        count = set()
        rowMin = 0
        colMin = 0
        rowMax = 0
        colMax = 0
        
        while rowMax != 9 and colmax != 9: 
            for i in range(rowMin, rowMax):
                for j in range(colMin, colMax):
                    board[i][j] 
            
        
        
# @lc code=end

