class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # sort the intervals with the 1 st and 2nd element

        def dfs(i, prev):
            if i == len(intervals): # i超过最后 遍历完了
                return 0
            res = dfs(i + 1, prev) # 分支1：不选第i个区间
            if prev == -1 or intervals[prev][1] <= intervals[i][0]: 
                # no prev or 上一个区间右 小于 这个区间左，不重叠，选了
                res = max(res, 1 + dfs(i + 1, i)) # 不选和选中更好的
            return res

        return len(intervals) - dfs(0, -1)    