class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums) - 1)
        candidate = 0

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        candidate = dp[-1]
        
        dp[0] = nums[len(nums) - 1]
        dp[1] = max(nums[len(nums) - 2], nums[len(nums) - 1])
        
        for j in range(2, len(nums) - 1):
            dp[j] = max(dp[j - 2] + nums[len(nums) - (j + 1)], dp[j - 1])
        
        return max(dp[-1], candidate)