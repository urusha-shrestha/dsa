# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
from collections import deque

class MyStack:
    
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        if self.q1:
            return(self.q1.popleft())
    
    def top(self):
        if self.q1:
            return self.q1[0]
        return None
    
    def empty(self):
        if self.q1:
            return False
        return True
    
obj = MyStack()
obj.push(1)
print(obj.pop())