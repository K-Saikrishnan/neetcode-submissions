class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # compute rolling calc to prevent overflow
        missing = len(nums)

        for i, num in enumerate(nums):
            missing += (i - num)
        
        return missing