# https://leetcode.com/problems/trapping-rain-water/solution/


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans, current = 0, 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[len(stack) - 1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = current - stack[len(stack) - 1] - 1
                bounded_height = min(height[current], height[stack[len(stack) - 1]]) - height[top]
                ans += distance * bounded_height
            stack.append(current)
            current += 1
        return ans



data = [0,1,0,2,1,0,1,3,2,1,2,1]
data2 = [1,0,0,0,0,2,0,0,0,4,1]
print(Solution().trap(data2))