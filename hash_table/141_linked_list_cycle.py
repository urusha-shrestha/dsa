# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

def hasCycleTwoPointer(head):
    slow, fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

def hasCycleHashMap(head):
    visited = set()
    temp = head

    while temp:
        if temp in visited:
            return True
        visited.add(temp)
        temp = temp.next
    
    return False

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

n1 = Node(3)     
n2 = Node(7)  
n3 = Node(2)  
n4 = Node(9)

LL = LinkedList()
LL.head = n1 
n1.next = n2
n2.next = n3
n3.next = n4 
n4.next = None 

print(hasCycleHashMap(n1))
