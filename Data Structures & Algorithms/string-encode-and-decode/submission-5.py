class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        
        return ans


    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []

        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            
            length = int(num)

            ans.append(s[i+1:i+1+length])

            i += 1 + length

        
        return ans
            