import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited = set()

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))
        
        total_cost = 0
        minH = [[0, 0]]
        while len(visited) < len(points):
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            total_cost += cost
            visited.add(i)
            for n_cost, neighbor in adj_list[i]:
                if neighbor not in visited:
                    heapq.heappush(minH, [n_cost, neighbor])
        return total_cost