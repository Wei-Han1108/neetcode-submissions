class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #必须是最大的或者至少比一个大
        good = set() # 结果集合， 非重复

        for t in triplets: 
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # if the first is bigger 
            for i, v in enumerate(t): # 
                if v == target[i]:
                    good.add(i)
        return len(good) == 3