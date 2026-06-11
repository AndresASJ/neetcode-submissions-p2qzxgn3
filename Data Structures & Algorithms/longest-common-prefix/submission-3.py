class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  #edge case of empty strings
            return ""
        
        for i in range(len(strs[0])): #get the len of the first word and interate in just that word
            char = strs[0][i]   #first string in the array and its first letter
            for j in strs[1:]: #look the second string in the array
                if  i == len(j) or char != j[i]: #if the other words are long than the first word or doesnt not match
                    return strs[0][:i] #return the first word and how ever long we go with it

        return strs[0] #if it fully passes the prefix should just be the master word