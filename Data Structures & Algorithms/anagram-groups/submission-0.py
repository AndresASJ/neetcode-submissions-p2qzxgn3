class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}
        for word in strs:
            key = "".join(sorted(word))

            if key in anagram_group:
                anagram_group[key].append(word)
            else:
                anagram_group[key] = [word]

        return list(anagram_group.values())