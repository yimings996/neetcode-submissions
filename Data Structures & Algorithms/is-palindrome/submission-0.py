# Time: O(n), O(n) creating s1, and loop through s1 from 2 pointers.
# Space: O(n) for s1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s1)-1
        while i < j:
            if s1[i] != s1[j]:
                return False
            i+=1
            j-=1
        
        return True
        