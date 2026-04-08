class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = None
        count = 0

        for x in nums:
            if count == 0:
                winner = x
            if winner == x:
                count +=1
            else:
                count -=1
        return winner