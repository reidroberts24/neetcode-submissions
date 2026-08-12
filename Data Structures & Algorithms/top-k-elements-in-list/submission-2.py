class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        h = []
        for n, count in counts.items():
            heapq.heappush(h, [count, n])
            if len(h) > k:
                heapq.heappop(h)
        return [count[1] for count in h]