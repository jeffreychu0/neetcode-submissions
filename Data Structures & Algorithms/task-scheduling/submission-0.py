class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)

        max_heap = [cnts for cnts in cnt.values()]
        heapq.heapify_max(max_heap)
        q = deque() # [cnt, idleTime]
        time = 0

        while max_heap or q:
            time += 1
            
            if not max_heap:
                time = q[0][1]

            else:
                curr_cnt = heapq.heappop_max(max_heap)
                curr_cnt -= 1

                if curr_cnt:
                    q.append([curr_cnt, time + n])
                

            if q and q[0][1] == time:
                heapq.heappush_max(max_heap, q.popleft()[0])

        return time
            