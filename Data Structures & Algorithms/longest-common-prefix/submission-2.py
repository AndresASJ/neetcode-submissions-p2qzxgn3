class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):  #Run through each char in the list
            char = strs[0][i] #start at the first string in the list
            for j in strs[1:]: #skip the first string in the list
                if i == len(j) or char != j[i] : #if char doesnt agree with j on that letter then
                    return strs[0][:i] #return everything until there
        return strs[0]