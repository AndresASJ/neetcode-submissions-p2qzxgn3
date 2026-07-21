class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
                print(f"this is inputted height {heights[i]} and this is the expected heights {expected[i]}")
        return count