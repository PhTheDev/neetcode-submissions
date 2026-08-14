class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxheight = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxheight = max(maxheight, area)

            if heights[l] < heights[r]:
                l += 1
                continue
            else:
                r -= 1
                continue

        return maxheight