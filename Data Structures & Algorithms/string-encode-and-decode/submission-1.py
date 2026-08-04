class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string
        
        return res


    def decode(self, s: str) -> List[str]:
        i = 0

        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i, j = j + 1 + length, j + i + length
        return res