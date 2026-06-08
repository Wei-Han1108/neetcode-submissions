import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 最大堆k大小的顶上就是
        self.heap = nums
        heapq.heapify(self.heap)
        length = len(nums)
        while length > k:
            heapq.heappop(self.heap)
            length -= 1
        return self.heap[0]
