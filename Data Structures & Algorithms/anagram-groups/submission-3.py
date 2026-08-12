class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i, word in enumerate(strs):
            str_sorted = tuple(sorted(word))
            if str_sorted in anagrams:
                anagrams[str_sorted].append(word)
            else:
                anagrams[str_sorted] = [word]
        
        return list(anagrams.values())
