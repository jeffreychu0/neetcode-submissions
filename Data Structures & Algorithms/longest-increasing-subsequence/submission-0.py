class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [0,4,2,3,2,2,1]
        # i  = [9,1,4,2,3,3,7]
        
        # dp = [0,4,3,2,3,2,1]
        # i  = [9,2,3,4,2,3,7]

        # lets say we go through from i=(n-1,-1), then dp[index] is the largest dp[i] of any value greater than its value. 
        # is there a non O(n^2) solution? 
            # Bottom up, we can calculate which values are larger than the value as another option, but that might be hard
            # feels as if we need a stack to solve this problem

        '''
        Issue with my intuition: I had went the wrong way. you're supposed to go left to right instead of right to left for this problem to solve it properly. 
        '''

        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            LIS = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS

        return max(dfs(i) for i in range(n))

        