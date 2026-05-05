class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        elem = [0] * n #new array
        rightMax = -1 #start at -1
        for i in range(n-1, -1,-1): #back to front
            elem[i] = rightMax  #first replace | Then save current rightMax
            rightMax = max(arr[i], rightMax)
        return elem
