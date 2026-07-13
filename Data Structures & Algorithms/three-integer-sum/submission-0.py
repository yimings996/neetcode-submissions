class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0 and ([nums[i], nums[j], nums[k]] not in res):
                    res.append([nums[i], nums[j], nums[k]])
                elif sum_ < 0:
                    j +=1
                else:
                    k -=1
        
        return res

                    