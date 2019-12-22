# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size_of_nums = len(nums)
        for i in range(size_of_nums):
            remainder = target - nums[i]
            for j in range(i+1, size_of_nums):
                if nums[j] == remainder:
                    return [i, j]
        return [-1, -1]

    def twoSum_version2(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


s = Solution()
test1 = ([2, 7, 11, 15], 9, [0, 1])
test2 = ([25, 5, 14, 8, 6, 3, 4], 18, [2, 6])
test3 = ([3,2,4],6,[1,2])

x1 = s.twoSum(list(test1[0]), test1[1])
x2 = s.twoSum_version2(list(test2[0]), test2[1])
assert x1 == list(test1[2])
assert x2 == list(test2[2])

x3 = s.twoSum(list(test3[0]), test3[1])
assert x3 == list(test3[2])