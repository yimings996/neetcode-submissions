class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        for i in range(n):
            temp = 0
            count = 0
            for j in range(i+1, n):
                temp += 1
                if temperatures[j] > temperatures[i]:
                    count = temp
                    break
            res.append(count)
        
        return res




        