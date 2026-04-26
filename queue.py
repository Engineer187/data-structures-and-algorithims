class Queue():
    def __init__(self,size):
        self.list=[]
        self.size=size
        self.avalable=size
    def enqueue(self,item):
        if len(self.list)==self.size:
            print("queue overflow")
        else:
            self.list.append(item)
    def dequeue(self):
        if len(self.list)==0:
            print("queue underflow")
        else:
            self.list.pop(0)
    def display(self):
        for i in range(len(self.list)):
            print(self.list[i])
queue=Queue(2)
queue.dequeue()
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(7)
queue.display()
queue.dequeue()
queue.display()
