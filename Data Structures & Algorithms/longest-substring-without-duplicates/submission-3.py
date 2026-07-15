# Time: O(n) for looping through the string once
# Space: O(m) for each unique characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        hs = set()
        cur = 0
        res = 0

        while j<len(s):
            if s[j] not in hs:
                hs.add(s[j])
                cur += 1
                j+=1
                res = max(cur, res)
            else:
                while s[j] in hs:
                    hs.remove(s[i])
                    i += 1
                    cur -= 1

                res = max(cur, res)


        return max(res, cur)
