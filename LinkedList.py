
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, val):
        self.head = ListNode(val)
    
    def insert_node(self, val):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = ListNode(val)
    
    def delete_node(self, val):
        current = self.head
        if current.val == val:
            # Head needs to be deleted
            self.head = current.next
            return
        # At this point we know its not the head
        previous = self.head
        while(current != None):
            if current.val == val:
                # This is the node to delete
                previous.next = current.next
                break
            previous = current
            current = current.next


    def reverse_list(self):
        current = self.head
        previous = None        
        while(current != None):
            next = current.next
            current.next = previous
            previous = current
            current = next            
        self.head = previous           

    def print_list(self):
        current = self.head
        while(current != None):
            print(current.val)
            current = current.next

list = LinkedList(1)
list.insert_node(2)
list.insert_node(3)
list.insert_node(4)

list.print_list()
print("Reversing List")
list.reverse_list()
list.print_list()
print("Deleting node")
list.delete_node(1)
list.print_list()
print("Deleting node again")
list.delete_node(4)
list.print_list()


