# Given the head of a singly linked list, reverse the list, and return the reversed list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(10)
b = ListNode(2)
c = ListNode(1)
d = ListNode(15)

a.next=b
b.next=c
c.next=d



def reverseLinkedList( head: ListNode)-> ListNode:
    prev,curr = None, head

    while curr:
        nxt = curr.next
        curr.next=prev
        prev=curr
        curr = nxt

    return prev


def print_list(node):
    while node is not None:
        print(f'{node.val} ', end='')
        node=node.next
    print()

print_list(reverseLinkedList(a))

