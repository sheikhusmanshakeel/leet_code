# https://leetcode.com/problems/contiguous-array/
# Key point here is how to initialise the dict. since we have to start counting from 0th index, we need to intialise with -1 index
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_so_far = 0
        count = 0
        h = {0: -1}
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in h:
                max_so_far = max(max_so_far, i - h[count])
            else:
                h[count] = i

        return max_so_far


data1 = [0, 1, 1, 0, 1, 1, 1, 0]
answer1 = 4
assert Solution().findMaxLength(data1) == answer1
