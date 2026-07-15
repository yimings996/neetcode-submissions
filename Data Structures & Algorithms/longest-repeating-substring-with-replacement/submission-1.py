# Time: O(n) loop through once only
# Space: O(n) for each character to store in hashmap

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hs = {}

        count = k
        res = 0

        i = 0
        j = 0

        while j < len(s):

            hs[s[j]] = hs.get(s[j], 0) + 1
            while j-i + 1 - max(hs.values()) > k:
                hs[s[i]] -= 1
                i+=1
            j+=1
            res = max(res, j - i)
        
        return res
        