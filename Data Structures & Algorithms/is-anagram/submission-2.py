class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        for letter in s:
            if letter in hm:
                hm[letter] += 1
            else:
                hm[letter] = 1
        
        for letter in t:
            if letter in hm:
                hm[letter] -= 1
            else:
                return False

        for i in hm:
            if hm[i]!=0:
                return False
        return True
