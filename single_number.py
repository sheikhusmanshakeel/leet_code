# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        x = nums[0]
        for i in range(1,len(nums)):
            x ^= nums[i]
        return x


s = Solution()
y = s.singleNumber([1])
print(y)
