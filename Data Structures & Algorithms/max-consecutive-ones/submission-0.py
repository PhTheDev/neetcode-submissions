class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        biggest = 0
        for n in nums:
            if n == 1:
                current += 1
                biggest = max(biggest, current)
            else:
                current = 0
        return biggest