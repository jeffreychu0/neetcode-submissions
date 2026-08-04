class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        ans = 0

        for elem in my_set:
            if elem-1 in my_set:
                continue
            else:
                count = 1
                curr = elem
                while curr + 1 in my_set:
                    curr += 1
                    count += 1
                ans = max(ans, count)
    
        return ans;
