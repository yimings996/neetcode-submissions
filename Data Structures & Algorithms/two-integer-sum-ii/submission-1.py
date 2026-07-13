# Time: O(n)
# Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        i = 0
        j = len(numbers)-1

        while i < j:
            _sum = numbers[i] + numbers[j]
            if _sum == target:
                return [i+1, j+1]
            elif _sum > target:
                j-=1
            else:
                i+=1
            
        return False
