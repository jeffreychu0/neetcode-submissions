class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        adj = [[] for _ in range(n)]

        self.is_tree = True

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node, prev):
            if node in visited:
                self.is_tree = False
                return
            
            visited.add(node)

            for adj_node in adj[node]:
                if prev is None:
                    dfs(adj_node, node)
                elif prev != adj_node:
                    dfs(adj_node, node)

        dfs(0, None)

        return self.is_tree and len(visited) == n
