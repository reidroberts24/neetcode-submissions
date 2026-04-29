class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #return k closest points to (0, 0)

        # create minheap of size k
        # calculate the dist of each point in the list
        # minheap contains the k smallest distances from (0,0)
        maxHeap = []

        for x, y in points:
            dist = -math.sqrt(x**2 + y**2)
            
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res

        