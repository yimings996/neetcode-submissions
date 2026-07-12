class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}

        if len(s) != len(t):
            return False

        for i in s:
            hm_s[i] = hm_s.get(i, 0) + 1
        

        for i in t:
            hm_t[i] = hm_t.get(i, 0) + 1

        return hm_s == hm_t