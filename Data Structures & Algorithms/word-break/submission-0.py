class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recursive approach: we would perform a dfs among the string if we find a match in keywords. if "cats" starts off the word and there is "cats", we can perform dfs among the entire substring "incars" and continue. 
        # could we do this from the top-down. starting from the last four letters. if there is no value that it could fit in, then we immediately return false? 
        # alternatively, is there a way to maintain indexed values to say "after index 3, we know its a string??"

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]