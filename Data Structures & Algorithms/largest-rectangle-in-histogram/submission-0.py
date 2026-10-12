class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pairs = list(enumerate(heights))
        stack = []
        left_len = [0] * len(heights)
        right_len = [0] * len(heights)
        

        for i in range(len(heights)):
            index, height = pairs[i]
            
            while stack and stack[-1][1] >= height:
                stack.pop()
            
            if stack:
                left_len[i] = index - stack[-1][0] - 1
            else:
                left_len[i] = index
            
            stack.append((index, height))

        stack = []

        for i in range(len(heights)-1, -1, -1):
            index, height = pairs[i]
            
            while stack and stack[-1][1] >= height:
                stack.pop()
            
            if stack:
                right_len[i] = stack[-1][0] - index - 1
            else:
                right_len[i] = len(heights) - index - 1
            
            stack.append((index, height))

        max_rec = 0
        
        for i in range(len(heights)):
            width = left_len[i] + right_len[i] + 1
            area = width * heights[i]

            max_rec = max(max_rec, area)
        
        return max_rec
        


            

        

        
            
            
                    

        