class Solution:
    def numDecodings(self, s: str) -> int:
        
        # the recursive approach: (1012) = 10 + s(12), 
        # s(12) = 2 possible ways. 
        # we can dp store the s(12) as 2 ways. 
        # we can either take the string as is (2 letters) or take it as a single letter "1 letter" and jump to the next element. 

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
            