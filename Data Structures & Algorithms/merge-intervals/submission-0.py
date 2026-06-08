class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        output = [intervals[0]] # get all sorted pair and put the 1st item in

        # cmpare the last interval's right boundary in output
        # and the current start, get the larger one as right boundary
        for start, end in intervals:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output