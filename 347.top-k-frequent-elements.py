#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
        sorted_nums = sorted(count.items(), key=lambda x : x[1], reverse=True)
        
        return [num for num, _ in sorted_nums[:k]]
        
# @lc code=end

