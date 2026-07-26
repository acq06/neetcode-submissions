class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water_area = l * w

        left = 0
        right = len(heights) - 1
        max_water_area = 0

        while left < right:
            length = right - left
            width = min(heights[left], heights[right])

            water_area = length * width

            if max_water_area < water_area:
                max_water_area = water_area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water_area