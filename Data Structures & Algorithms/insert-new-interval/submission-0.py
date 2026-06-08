class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the minumun less than it, if there's not  if there's any
        # interval left point less than mine left or equal to, means need combine
        # same if the larger bigger than mine right or equal to, means combine
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0] # want to find the left edge
        left, right = 0, n - 1 # for the binary search edge
        
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target: # only search left boundry
                left = mid + 1
            else: 
                right = mid - 1
        
        intervals.insert(left, newInterval) # add anyway and clean after

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1]) # update every right bounday of -1 index (newest index)
        return res