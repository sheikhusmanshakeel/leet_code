from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def dedup(self, root: ListNode) -> List[ListNode]:
        print("do something")
        current = root
        prev = None
        seen = {}
        while current.next != None:
            if current.val in seen:
                prev.next = current.next
            else:
                seen[current.val] = current.val
                prev = current

            current = current.next

        return root




root = ListNode(5)
root.next = ListNode(5)
root.next.next = ListNode(5)
root.next.next.next = ListNode(5)

# root = ListNode(5)
# root.next = ListNode(3)
# root.next.next = ListNode(7)
# root.next.next.next = ListNode(5)
# root.next.next.next.next = ListNode(3)
# root.next.next.next.next.next = ListNode(1)
# root.next.next.next.next.next.next = ListNode(0)
# root.next.next.next.next.next.next.next = ListNode(12)

Solution().dedup(root)