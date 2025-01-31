#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, 0, 1, 2]
        sortedNums = sorted(nums)
        numSet = set(sortedNums)
        
        for a in nums:
            l = 0
            r = len(numSet)
            
            while l < r:
                b = numSet
            
        
        
# @lc code=end

 