from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kth_last_element(self, root: ListNode, k: int) -> int:
        current = root
        prev = root
        current_k = 0
        while current != None:
            if current_k < k:
                current = current.next
                current_k += 1
            else:
                prev = prev.next
                current = current.next
        return prev.val


root = ListNode(5)
root.next = ListNode(2)
root.next.next = ListNode(8)
root.next.next.next = ListNode(3)

data1 = 1
target1 = 3
retVal = Solution().kth_last_element(root, data1)
assert retVal == target1

root = ListNode(5)
root.next = ListNode(3)
root.next.next = ListNode(7)
root.next.next.next = ListNode(5)
root.next.next.next.next = ListNode(3)
root.next.next.next.next.next = ListNode(1)
root.next.next.next.next.next.next = ListNode(0)
root.next.next.next.next.next.next.next = ListNode(12)

data2 = 3
target2 = 1
retVal2 = Solution().kth_last_element(root, data2)
assert retVal2 == target2
