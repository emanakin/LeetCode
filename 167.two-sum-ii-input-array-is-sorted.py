#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            val = numbers[l] + numbers[r]
            
            if (val == target):
                return [l + 1, r + 1]
            elif (val > target):
                r -= 1
            elif (val < target):
                l += 1
            
            
        
# @lc code=end

