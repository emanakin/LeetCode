#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 0
        numSet = set(nums)
        
        for num in numSet:
            # when do we know when we have a seq?
            if ((num - 1) not in numSet):
                # track length
                length = 1
                nextNum = num + 1
                # increase if theres a consequtive int
                while (nextNum in numSet):
                    length += 1
                    nextNum += 1
                
                # updates longest recorded seq
                longestSeq = max(length, longestSeq)
        
        return longestSeq
        
        
# @lc code=end

