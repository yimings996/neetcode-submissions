# Time: O(n) loop through once only
# Space: O(n) for each character to store in hashmap

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hs = {}

        res = 0
        max_count = 0
        cur_count = 0

        i = 0
        j = 0

        while j < len(s):

            hs[s[j]] = hs.get(s[j], 0) + 1
            max_count = max(max_count, hs[s[j]])
            while j-i + 1 - max_count > k:
                hs[s[i]] -= 1
                i+=1
            j+=1
            res = max(res, j - i)
        
        return res
        