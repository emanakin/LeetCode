#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        larger_int = 0
        multiplier = 1
        
        for i in range(len(digits) - 1, -1, -1):
            larger_int += digits[i] * multiplier
            multiplier *= 10
            
        larger_int += 1
        
        return [int(digit) for digit in str(larger_int)]
        
        
# @lc code=end

