#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
            if count[num] > 1:
                return True    
        
        return False
        
        
# @lc code=end

