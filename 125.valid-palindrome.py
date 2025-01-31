#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stripped = ""
        
        for c in s:
            if c.isalnum():
                s_stripped += c.lower()
                
        l = 0
        r = len(s_stripped) - 1
        
        while l <= r:
            if s_stripped[l] != s_stripped[r]:
                return False
            l += 1
            r -= 1
            
        return True
        
# @lc code=end

