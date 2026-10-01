'''
class Stack:
    def __init__(self):
        self.s=[]
    def push(self,var):
        self.s.append(var)
    def is_empty(self):
        return len(self.s)==0
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.s.pop()
    def size(self):
        return len(self.s)
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.s[-1]
    
st=Stack()
print(st.is_empty())
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.size())
st.pop()
print(st.size())
print(st.peek())
'''
# Stack implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack_LL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            return "pop from empty stack"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count
    def peek(self):
        if self.is_empty():
            return "peek from empty stack"
        return self.top.data
    