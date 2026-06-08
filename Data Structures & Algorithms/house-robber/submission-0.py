class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev1 = 0
        prev2 = 0
        current = max(prev1, prev2)
        
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        
        return current