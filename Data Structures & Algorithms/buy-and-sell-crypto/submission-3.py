class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0
        # determine what the smallest left side is while getting the highest right side

        while r < len(prices):
            ans = max(ans, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        
        return ans