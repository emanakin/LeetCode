#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        minVal = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, minVal))

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[0]
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
         
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

