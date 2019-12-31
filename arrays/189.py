# https://leetcode.com/problems/rotate-array/


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return nums
        index = k % l
        if index == 0:
            return nums
        counter = 0
        start = l - index
        for i in range(start, l):
            nums.insert(counter, nums.pop(i))
            counter += 1
        return nums


data1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
answer1 = [5, 6, 7, 1, 2, 3, 4]
assert Solution().rotate(data1, k1) == answer1

data2 = []
k2 = 10
answer2 = []
assert Solution().rotate(data2, k2) == answer2

data3 = [1, 2, 3, 4, 5, 6, 7]
k3 = 7
answer3 = [1, 2, 3, 4, 5, 6, 7]
assert Solution().rotate(data3, k3) == answer3

data4 = [1, 2, 3, 4, 5, 6, 7]
k4 = 16
answer4 = [6, 7, 1, 2, 3, 4, 5]
assert Solution().rotate(data4, k4) == answer4

data5 = [-1,-100,3,99]
k5 = 2
answer5 = [3,99,-1,-100]
assert Solution().rotate(data5, k5) == answer5

