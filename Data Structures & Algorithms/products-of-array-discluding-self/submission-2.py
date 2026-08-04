class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [1] * len(nums), [1] * len(nums)
        
        i, j = 1, len(nums) - 2

        while i < len(nums):
            pre[i] = pre[i-1] * nums[i-1]
            suf[j] = suf[j+1] * nums[j+1]
            i += 1
            j -= 1

        return [pre[i] * suf[i] for i in range(len(pre))]
        
