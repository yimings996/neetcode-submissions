class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_hash = set()
        for i in nums:
            if i not in check_hash:
                check_hash.add(i)
            else:
                return True
        return False
