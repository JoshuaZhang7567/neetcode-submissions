class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_sorted = sorted(zip(position, speed))
        position, speed = zip(*paired_sorted)
        stack = []
        for i in range(len(position)-1, -1, -1):
            if not stack:
                stack.append(i)
            if (target-position[stack[-1]])/speed[stack[-1]] < (target-position[i])/speed[i]:
                stack.append(i)
        
        return len(stack)