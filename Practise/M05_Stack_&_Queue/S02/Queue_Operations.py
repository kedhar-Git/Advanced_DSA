#queue implementation using linked list
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class Queue_LL:
    def __init__(self):
        self.front=None 
        self.rear=None

    def enqueue(self,val):
        new_node = Node(val)
        if self.rear is None:
            self.rear=self.front=new_node
            return
        self.rear.next =new_node
        self.rear=new_node

    def dequeue(self):
        if self.is_empty():
            return "dequeue from empty queue"
        del_value=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return del_value 

    def peek(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data
    
    def display(self):
        if self.front is None:
            print("Queue is empty")
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
q=Queue_LL()
q.enqueue(10)
q.enqueue(100)
q.enqueue(1000)
q.enqueue(10000)
q.display()
q.dequeue()
q.display()
print(q.peak())