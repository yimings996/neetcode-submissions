# Note: use frequencies wisely as storing frequency of chars is O(26)
# not dependent on n.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hm1 = {}
        hm2 = {}
        
        for i in s1:
            hm1[i] = hm1.get(i, 0) + 1
        
        for i in range(len(s1)):
            hm2[s2[i]] = hm2.get(s2[i], 0) + 1
        
        if hm2 == hm1:
                return True
        i = 0
        j = len(s1)
        while j < len(s2):
            hm2[s2[j]] = hm2.get(s2[j], 0) + 1

            hm2[s2[i]] = hm2[s2[i]] - 1
            if hm2[s2[i]] == 0:
                del(hm2[s2[i]])
            i += 1
            if hm2 == hm1:
                return True
            j+=1
        
        return False
        