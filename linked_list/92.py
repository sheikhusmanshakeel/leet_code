# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        fixed = dummyNode

        for i in range(m - 1):
            fixed = fixed.next

        prev = None
        curr = fixed.next
        for i in range(n - m + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        fixed.next.next = curr
        fixed.next = prev

        return dummyNode.next



root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(7)
m = 1
n = 3
ans = Solution().reverseBetween(root, m, n)
print(ans)

