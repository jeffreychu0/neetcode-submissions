class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1

        # determine what the smallest left side is while getting the highest right side

        left_min = prices[0]
        right_max = prices[len(prices) - 1]

        while l < r:
            left_diff = prices[l+1] - prices[l]
            right_diff = prices[r] - prices[r-1]

            if left_diff <= right_diff:
                l += 1
                left_min = min(left_min, prices[l])
            else:
                r -= 1
                right_max = max(right_max, prices[r])
            


        return max(right_max - left_min, 0)