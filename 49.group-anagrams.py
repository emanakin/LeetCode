#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())
            
# @lc code=end

