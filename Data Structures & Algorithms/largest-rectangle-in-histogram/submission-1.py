class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0

        for i in range(len(heights)):
            left_stack = [i]
            right_stack = [i]

            while left_stack[-1] - 1 >= 0 and heights[left_stack[-1] - 1] >= heights[i]:
                left_stack.append(left_stack[-1]-1)
            while right_stack[-1] + 1 < len(heights) and heights[right_stack[-1]+1] >= heights[i]:
                right_stack.append(right_stack[-1]+1)  

            rectangle = (len(left_stack) + len(right_stack) - 1)*heights[i]
            if rectangle > largest:
                largest = rectangle

        return largest
                

