class Stack():
    def __init__(self,max):
        self.list=[]
        self.size=max
    def push(self,item):
        if len(self.list)<self.size:
            self.list.append(item)
        else:
            print("start overflow")
    def pop(self):
        if len(self.list)==0:
            print("stack underflow")
        else:
            self.list.pop(-1)
    def peek(self,top):
        top=self.list(-1)
        return top
    def display(self):
        for i in range(len(self.list)-1,-1,-1):
            print(self.list[i])

stack=Stack(3)
stack.push(5)
stack.push(8)
stack.push(1)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()