from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        ans = []

        bucket_list = [[] for _ in range(len(nums))]

        for key, val in freq.items():
            bucket_list[val - 1].append(key)

        for i in range(len(bucket_list), 0, -1):
            for val in bucket_list[i-1]:
                ans.append(val)
        
        return ans[:k]