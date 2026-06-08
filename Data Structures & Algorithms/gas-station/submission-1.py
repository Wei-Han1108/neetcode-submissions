class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # sum function 
            return -1
         
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # find the only start point

            if total < 0: # if < 0 must not start point
                total = 0
                res = i + 1
        
        return res