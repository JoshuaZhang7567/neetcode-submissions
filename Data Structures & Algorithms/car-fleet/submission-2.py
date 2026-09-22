class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_sorted = sorted(zip(position, speed), reverse=True)
        stack = []
        for position, speed in paired_sorted:
            if not stack:
                stack.append((target-position)/speed)
            if stack [-1] < (target-position)/speed:
                stack.append((target-position)/speed)
        
        return len(stack)