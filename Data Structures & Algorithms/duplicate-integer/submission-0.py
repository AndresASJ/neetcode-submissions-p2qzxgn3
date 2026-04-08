class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compare = set()
        for i in nums:
            if i in compare:
                return True
            else:
                compare.add(i)
        return False
