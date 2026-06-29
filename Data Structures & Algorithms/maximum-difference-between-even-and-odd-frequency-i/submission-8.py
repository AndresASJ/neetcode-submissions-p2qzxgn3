class Solution:
    def maxDifference(self, s: str) -> int:
        seenMap = {}
        a1,a2 = 0 , float("inf")
        
        for key in (s):
            seenMap[key] = seenMap.get(key,0)+1

        for count in seenMap.values():
            if count % 2 == 1:
                a1 = max(a1,count)
            else:
                a2 = min(a2,count)
        
        first = max(a1,a2)
        second = min(a1,a2)
        
        
        print(seenMap)  
        return a1-a2
