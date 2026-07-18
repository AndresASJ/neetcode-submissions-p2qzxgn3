class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            result = int(i[11:-2])
            if result > 60:
                count +=1 
        return count