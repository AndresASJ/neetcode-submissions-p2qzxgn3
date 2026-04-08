class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        ans = []
        i =0
        while n != 0:
            ans.append(nums[i % len(nums)])
            i +=1
            n -=1
        return ans