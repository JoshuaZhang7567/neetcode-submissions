class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lower = 0
        upper = len(numbers)-1

        for i in range(len(numbers)):
            bot = numbers[lower]
            top = numbers[upper]
            if bot + top == target:
                return [lower+1, upper+1]
            if bot + top > target:
                upper -= 1
            if bot + top < target:
                lower += 1
        return []

