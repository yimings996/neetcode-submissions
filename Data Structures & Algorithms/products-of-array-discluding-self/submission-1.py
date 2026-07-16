class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n

        prefix = 1

        suffix = 1

        for i in range(1, n):
            res[i] *= prefix * nums[i-1]
            prefix *= nums[i-1]

            res[n-i-1] *= suffix * nums[n - i]
            suffix *= nums[n-i]


        return res


        