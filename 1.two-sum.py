#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = {}
        
        for ind, num in enumerate(nums):
            missing_val = target - num
            
            if missing_val in count:
                return [count[missing_val], ind]
            else:
                count[num] = ind
                continue
            
        return []
        
# @lc code=end

