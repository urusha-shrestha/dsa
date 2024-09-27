class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

a1.next=a2
a2.next=a3
b1.next=b2
b2.next=b3

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

def mergeTwoLists(l1, l2):
    #using two pointers one in l1 and one in l2 to compare the values
    #adding the small value to new listnode and updating the current pointer to the next one 
    dummy = ListNode()
    nxt = dummy

    while l1 and l2:
        if l1.val < l2.val:
            nxt.next = l1
            l1 = l1.next
        else:
            nxt.next = l2
            l2 = l2.next
        nxt = nxt.next
    
    if l1:
        nxt.next = l1
    elif l2:
        nxt.next = l2

    return dummy.next   


print(mergeTwoLists(a1,b1))