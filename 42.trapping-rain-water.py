#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        res = 0
        
        maxLeft = height[l]
        maxRight = height[r]
        
        while l < r:
            if maxLeft < maxRight:
                res += min(maxLeft, maxRight) - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                res += min(maxLeft, maxRight) - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
                
        return res
        
# @lc code=end

