class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # length控制len长度，从末尾开始对比
        # x == y: length - 2， if not: length - 1 and stones[length] = max(x, y) - min(x, y)
        if len(stones) == 1:
            return stones[0]
        end = len(stones) - 1
        while(end > 0):
            stones.sort()
            x = stones[end - 1]
            y = stones[end]
            if x == y:
                end -= 2
                if end == -1:
                    return 0
            else:
                end -= 1
                stones[end] = max(x, y) - min(x, y)
        return stones[0]


