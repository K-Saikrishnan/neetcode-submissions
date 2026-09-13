class Solution:
    def climbStairs(self, n: int) -> int:
        # Space-optimized
        one, two = 1, 0

        for _ in range(n):
            one, two = one+two, one
        
        return one