# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    temp = l1.val + l2.val
    carry = temp // 10
    output = ListNode(temp % 10)
    output_head = output
    l1 = l1.next
    l2 = l2.next
    while (l1 is not None) or (l2 is not None):
        l1_val = 0
        l2_val = 0
        if l1 is not None:
            l1_val = l1.val
            l1 = l1.next
        if l2 is not None:
            l2_val = l2.val
            l2 = l2.next
        temp = l1_val + l2_val + carry
        carry = temp // 10
        output.next = ListNode(temp % 10)
        output = output.next

    if carry != 0:
        output.next = ListNode(carry)
    return output_head


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(8)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

l1 = ListNode(6)
l2 = ListNode(5)

l3 = add_two_numbers(l1, l2)
print(l3)
