class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)

            heapq.heappush_max(stones, abs(a - b))
        
        return stones[0]

