class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        answer = Counter("balloon")
        result = len(text)
        for i in answer:
            result = min(result, counts[i] // answer[i])
        return result