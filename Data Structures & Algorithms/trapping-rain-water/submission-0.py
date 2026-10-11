class Solution:
    def trap(self, height: List[int]) -> int:
        left_high = [-1] * len(height)
        
        for i in range(1, len(height)):
            if left_high[i-1] >= height[i-1]:
                left_high[i] = left_high[i-1]
            else:
                left_high[i] = height[i-1]
            
        right_high = [-1] * len(height)

        for i in range(len(height)-2, -1, -1):
            if right_high[i+1] >= height[i+1]:
                right_high[i] = right_high[i+1]
            else:
                right_high[i] = height[i+1]
        
        sum = 0

        for i in range(len(height)):
            mi = min(left_high[i], right_high[i])
            if mi > height[i]:
                sum+= mi - height[i]
            
        
        return sum
            

        