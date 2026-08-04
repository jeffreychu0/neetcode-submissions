from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        print(freq)

        sorted_k_elems = []

        for key, val in freq.items():
            sorted_k_elems.append((val, key))
        
        sorted_k_elems = sorted(sorted_k_elems, reverse=True)

        return [x[1] for x in sorted_k_elems[:k]]