class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [1] * len(nums), [1] * len(nums)

        i = 1
        j = len(nums) - 2

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
            suf[j] = suf[j+1] * nums[j+1]
            j -= 1

        ans = [1] * len(nums)

        for i in range(len(ans)):
            ans[i] = pre[i] * suf[i]

        return ans

