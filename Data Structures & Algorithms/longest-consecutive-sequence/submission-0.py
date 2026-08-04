class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0

        for num in set_nums:
            if num - 1 in set_nums:
                continue
            else:
                count = 1
                j = num
                while j + 1 in set_nums:
                    count += 1
                    j += 1

                ans = max(count, ans)
        
        return ans