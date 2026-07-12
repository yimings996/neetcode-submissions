# keep aware of the index and actual value, when to use which
# Time: O(n), one single loop through nums and avg of O(1) for get
# Space: O(n), store at most n items into indexs
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexs:
                return [indexs[diff], i]
            else:
                indexs[nums[i]] = i
            

            

        