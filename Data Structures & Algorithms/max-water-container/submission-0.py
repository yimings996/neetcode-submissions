# Time: O(n) as only loop through the heights list one time
# Space: O(1)
# Note: try to start thinking from the brute force approach and
# link to the features of the problem, like the pairing of index.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights)-1

        while i<j:
            area = min(heights[i], heights[j]) * (j-i)
            if area > res:
                res = area

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        
        return res
            



        