import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 负数的最小堆就是最大堆
        # 最大堆每次拿出顶部两个
        # 不一样大就再push进去一个
        # 直到最后为0个就返回0，为一个就返回 - heap[0]
        self.heap=[-s for s in stones]
        heapq.heapify(self.heap)
        while len(self.heap) > 1:
            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)
            if x != y:
                heapq.heappush(self.heap, x - y) # - 15 - -5 = - 10
        # 记得加-
        return -self.heap[0] if self.heap else 0
        