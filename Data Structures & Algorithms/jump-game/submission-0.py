class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # just add -  too many poosible
        # from back to see if there's any from 
        def dfs(i):
            if i == len(nums) - 1: # already last
                return True
            end = min(len(nums) - 1, i + nums[i]) # try all the possible here
            for j in range(i + 1, end + 1): # 
                if dfs(j): 
                    return True
            return False

        return dfs(0)  

        