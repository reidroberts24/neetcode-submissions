class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i: [] for i in range(n)}

        for neighbor_1, neighbor_2 in edges:
            adj[neighbor_1].append(neighbor_2)
            adj[neighbor_2].append(neighbor_1)

        def dfs(cur, start_node):
            time = 0
            for node in adj[cur]:
                if node == start_node:
                    continue
                child_time = dfs(node, cur)
                if child_time > 0 or hasApple[node] is True:
                    time += 2 + child_time
            return time
        
        return dfs(0, -1)