#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        base = len(height) - 1
        l = 0
        r = len(height) - 1
        res = base * min(height[l], height[r]) 
        
        while l < r:
            if height[l] > height[r]:
                r -= 1
                base -= 1
            else:
                l += 1
                base -= 1
                
            res = max(res, base * min(height[l], height[r]))
        
        return res
    
# @lc code=end

