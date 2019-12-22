# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        is_even = (l1+l2) % 2 == 0
        med1 = int((l1+l2)/2)
        med2 = med1 + 1
        current_count = 0
        if l1 > l2:
            for i in range(l1):
                if 




n1 = [1,2,4,6,7]
n2 = [3,9]
s = Solution().findMedianSortedArrays(list(n1),list(n2))