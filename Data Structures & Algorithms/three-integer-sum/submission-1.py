# Time: O(n^2)
# Space: O(1)
# Note: need to skip duplicates by doing typical while loop skip for pointers.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0 and ([nums[i], nums[j], nums[k]] not in res):
                    res.append([nums[i], nums[j], nums[k]])
                elif sum_ < 0:
                    j+=1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j+=1
                else:
                    k -=1
                    while k >i and nums[k] == nums[k+1]:
                        k-=1
        
        return res

                    