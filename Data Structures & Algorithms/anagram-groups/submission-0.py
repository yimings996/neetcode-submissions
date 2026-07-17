class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hs = {}
        for i in range(len(strs)):
            new = ''.join(sorted(strs[i]))
            if new in hs:
                (hs[new]).append(strs[i])
            else:
                hs[new] = [strs[i]]        

        return list(hs.values())

        