class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_dp = [0] * len(cost)

        min_cost_dp[0] = cost[0]
        min_cost_dp[1] = cost[1]

        for i in range(2, len(cost)):
            min_cost_dp[i] = min(min_cost_dp[i-2], min_cost_dp[i-1]) + cost[i]

        return min(min_cost_dp[len(cost) - 1], min_cost_dp[len(cost) - 2])