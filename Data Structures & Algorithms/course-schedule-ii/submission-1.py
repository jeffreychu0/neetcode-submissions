class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for src, dst in prerequisites:
            indegree[src] += 1
            adj[dst].append(src)

        print(adj)

        order = []
        q = deque()

        for i, prereq in enumerate(indegree):
            if prereq == 0:
                q.append(i)

        while q:
            course = q.popleft()

            order.append(course)

            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            

        print(order)
        if len(order) != numCourses:
            return []

        return order