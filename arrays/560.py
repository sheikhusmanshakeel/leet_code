# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        h = dict()
        h[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - k) in h:
                count += h[sum - k]
            if sum in h:
                h[sum] = (h[sum]) + 1
            else:
                h[sum] = 1
        return count


data1 = [1, 1, 1]
target1 = 2
answer1 = 2

data2 = [3, 4, 7, 2, -3, 1, 4, 2]
target2 = 7
answer2 = 4

data3 = [4, 1, -6, 3, 9, -2, 4, 8, 2, 0, -5, 7]
target3 = 2
answer3 = 5

# assert Solution().subarraySum(data1, target1) == answer1
# assert Solution().subarraySum(data2, target2) == answer2
assert Solution().subarraySum(data3, target3) == answer3
