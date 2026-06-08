import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # ksize的最小堆的顶部是第k大的
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 加一个更大的就是在heap替换最小的
        if len(self.heap) < self.k:
            # push need self.heap
            heapq.heappush(self.heap, val)
        # compare with top not k
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
