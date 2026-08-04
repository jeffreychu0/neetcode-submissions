class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [1] * len(nums), [1] * len(nums)
        i, j = 0, len(nums) - 1
        
        while i < len(nums) - 1:
            pre[i + 1] = pre[i] * nums[i]
            suf[j - 1] = suf[j] * nums[j]
            
            i += 1
            j -= 1

        ans = [1] * len(nums)

        for i in range(len(ans)):
            ans[i] = pre[i] * suf[i]
        
        return ans
    #  [1, 1, 2, 8] 
    #     [1, 2, 4, 6]
    #        [48, 24, 6, 1]

