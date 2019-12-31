# https://leetcode.com/problems/split-linked-list-in-parts/
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ll_len = 0
        curr = root
        list_of_ll = []
        while curr:
            ll_len += 1
            curr = curr.next

        curr = root
        new_curr = None
        width, rem = divmod(ll_len,k)

        for i in range(k):
            new_head = curr
            for j in range(width + (i < rem) - 1):
                if curr:
                    curr = curr.next
            if curr:
                prev = curr
                curr = curr.next
                prev.next = None
            list_of_ll.append(new_head)
        return list_of_ll


root = ListNode(5)
root.next = ListNode(3)
root.next.next = ListNode(7)
# root.next.next.next = ListNode(2)
# root.next.next.next.next = ListNode(1)
# root.next.next.next.next.next = ListNode(8)
# root.next.next.next.next.next.next = ListNode(0)
# root.next.next.next.next.next.next.next = ListNode(12)
target = 6
ans = Solution().splitListToParts(root, target)
print(ans)
