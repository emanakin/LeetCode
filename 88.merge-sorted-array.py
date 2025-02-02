#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        for i, num_from_one in enumerate(nums1):
            num_from_two = nums2[i]
            
            if num_from_two > num_from_one:
                nums1.insert(i + 1, num_from_two)
            if num_from_two < num_from_one:
                nums1.insert(i, num_from_two)
            
        
# @lc code=end

