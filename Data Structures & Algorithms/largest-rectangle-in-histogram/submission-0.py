class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        neighbors = {}

        for i in range(len(heights)):
            width = 1

            # get the left
            temp_index = i-1
            while temp_index >= 0:
                if heights[temp_index] >= heights[i]:
                    width += 1
                    temp_index -= 1
                else:
                    break

            # get the right
            temp_index = i+1
            while temp_index < len(heights):
                if heights[temp_index] >= heights[i]:
                    width += 1
                    temp_index += 1
                else:
                    break

            neighbors[i] = width

        area = lambda l, w: l*w
        largest_area = 0
        for index, width in neighbors.items():
            largest_area = max(largest_area, area(heights[index], width))

        return largest_area

