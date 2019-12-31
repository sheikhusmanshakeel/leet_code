from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        if head and head.next:
            while curr:
                new_head = ListNode(curr.val)
                new_head.next = prev
                curr = curr.next
                prev = new_head
            return new_head
        else:
            return head


    def reverseList_recursion(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        t = self.reverseList_recursion(head.next)
        head.next.next = head
        head.next = None
        return t


# root = ListNode(5)
# root.next = ListNode(3)
# root.next.next = ListNode(7)
# root.next.next.next = ListNode(2)
# root.next.next.next.next = ListNode(1)
# root.next.next.next.next.next = ListNode(8)

root = ListNode(5)
root.next = ListNode(3)
root.next.next = ListNode(7)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(1)
root.next.next.next.next.next = ListNode(8)
Solution().reverseList_recursion(root)








