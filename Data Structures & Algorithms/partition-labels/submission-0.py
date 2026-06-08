class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # means get the first and last occur index
        lastIndex = {} 
        for i, c in enumerate(s):
            lastIndex[c] = i 
        # get lastindex dictionary of each 
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res

