class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for index in nums:
            if index in seen:
                return True
            else:
                seen.add(index)
        return False
