'''
#Queue implementation using python
class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,val):
        self.queue.append(val)

    def is_empty(self):
        return len(self.queue)==0

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
qu= Queue()
qu.enqueue(10)
qu.enqueue(100)
qu.enqueue(1000)
qu.enqueue(10000)
print(qu.is_empty())
print(qu.dequeue())
print(qu.front())    
'''