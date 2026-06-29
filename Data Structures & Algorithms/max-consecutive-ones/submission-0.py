class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxtotal = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
            else:
                current = 0
            maxtotal = max(maxtotal,current)
            
        return maxtotal