class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0

        for i in range(len(heights)):
            upper_limit = heights[i]
            for j in range(i, len(heights)):
                if upper_limit > heights[j]:
                    upper_limit = heights[j]
                rectangle_area = upper_limit * (j-i+1)

                if rectangle_area > answer:
                    answer = rectangle_area

        return answer
                

