import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-s for s in stones]
        heapq.heapify(self.heap)
        while len(self.heap) > 1:
            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)
            if x != y:
                heapq.heappush(self.heap, x - y)
        return -self.heap[0] if self.heap else 0