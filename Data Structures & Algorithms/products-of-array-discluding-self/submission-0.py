# Time: O(n) as first loop through 1 to n to compute prefix and suffix products
# Space: O(n) for creation of fron and back, both O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1]
        back = [1]

        for i in range(1, len(nums)):
            front.append(front[i-1] * nums[i-1])
            back.append(back[i-1] * nums[len(nums) - i])

        print(front)
        print(back)
        
        back.reverse()

        res = []

        for i in range(len(nums)):
            res.append(front[i] * back[i])

        return res
            