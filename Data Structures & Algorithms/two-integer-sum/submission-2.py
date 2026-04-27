class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for index, value in enumerate(nums):
            complement = target - value

            if complement in seenMap:
                return [seenMap[complement], index]

            seenMap[value] = index
        
        return False
    
