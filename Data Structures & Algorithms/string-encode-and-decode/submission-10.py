class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            encoded = str(len(s)) + "#" + s
            res += encoded
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # "5hello5world"
        
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1 
                word_len = int(s[j:i])
            end_index = i + 1 + word_len
            word = s[i + 1: end_index]
            res.append(word)
            i = end_index
        return res