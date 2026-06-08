import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # ksize最小堆第k大的是堆顶元素
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
            # 前k个最小的？


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # 比最小的大说明
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]