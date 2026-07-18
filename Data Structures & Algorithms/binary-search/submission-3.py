class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums)
        k = int((i+j) / 2)

        while i<=j and i<len(nums) and j>=0:
            if nums[k] == target:
                return k
            elif nums[k] < target:
                i = k + 1
                k = int((i+j) / 2)
            else:
                j = k - 1
                k = int((i+j) / 2)
            
        return -1
        