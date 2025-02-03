#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool: 
        
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in close_to_open:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
                
        if stack:
            return False
        else:
            return True
            
                
# @lc code=end

