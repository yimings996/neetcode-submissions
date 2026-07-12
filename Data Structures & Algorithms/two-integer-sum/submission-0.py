class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexs:
                return [indexs[diff], i]
            else:
                indexs[nums[i]] = i
            

            

        