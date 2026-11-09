class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def dfs(amount):
            res = float('inf')
            if amount in memo:
                return memo[amount]
            
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, (dfs(amount - coin) + 1))
            
            memo[amount] = res
            return res
                
        res = dfs(amount)

        if res == float('inf'): 
            return -1
        else: 
            return res