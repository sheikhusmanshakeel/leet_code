# https://leetcode.com/problems/rotate-list/

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        len_of_list = 0
        curr = head
        while curr:
            curr = curr.next
            len_of_list += 1
        cut_off_point = k % len_of_list if len_of_list else 0
        if len_of_list == 0 or cut_off_point == 0 or len_of_list == 1:
            return head
        fast, new_tail = head, head
        while cut_off_point > 0:
            fast = fast.next
            cut_off_point -= 1
        while fast.next:
            fast = fast.next
            new_tail = new_tail.next
        new_head = curr = new_tail.next
        while curr and curr.next:
            curr = curr.next
        curr.next = head
        new_tail.next = None
        return new_head





root = ListNode(1)
root.next = ListNode(2)
# root.next.next = ListNode(3)
# root.next.next.next = ListNode(4)
# root.next.next.next.next = ListNode(5)
# root.next.next.next.next.next = ListNode(6)
k = 0
ans = Solution().rotateRight(root, k)
print(ans)


