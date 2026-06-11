class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
         
        else:
            plan_a = self.rob_linear(nums[:-1])
            plan_b = self.rob_linear(nums[1:])
            return max(plan_a, plan_b)

    def rob_linear(self, houses: list[int]) -> int :
        prev1 = 0
        prev2 = 0
    
        for money in houses:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1

            
