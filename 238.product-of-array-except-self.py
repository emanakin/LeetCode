#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        
        # [48, 24, 6, 0]
        postfix = [0] * N
        
        # [0, 1, 2, 8]
        prefix = [0] * N
        
        total = 1
        for i in range(N - 2, -1, -1):
            total *= nums[i + 1]
            postfix[i] = total
        
        total = 1
        for i in range(1, N):
            total *= nums[i - 1]
            prefix[i] = total
            
        postfix[N - 1] = prefix[0] = 1
        for i in range(N):
            res.append(postfix[i] * prefix[i])
            
        return res
        
# @lc code=end

