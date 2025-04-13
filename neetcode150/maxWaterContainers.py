def maxArea(heights: list) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, current_area)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_area