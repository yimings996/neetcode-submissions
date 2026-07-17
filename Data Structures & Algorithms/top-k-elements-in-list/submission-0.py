class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for i in range(n+1)] 
        freq = {}
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for i in freq:
            (bucket[freq[i]]).append(i)
        
        count = 0
        res = []
        j = n
        
        while j>=0:
            res += bucket[j]            
            j -= 1

        
        return res[:k]

        