class Tree():
    def __init__(self,value):
        self.value=value
        self.leftchild=None
        self.rightchild=None
    def preorder(self):
        print(self.value)
        if self.leftchild != None:
            self.leftchild.preorder()
        if self.rightchild != None:
            self.rightchild.preorder()
    def inorder(self):
        if self.leftchild != None:
            self.leftchild.inorder()
        print(self.value)
        if self.rightchild != None:
            self.rightchild.inorder()
    def postorder(self):
        if self.leftchild != None:
            self.leftchild.postorder()
        if self.rightchild != None:
            self.rightchild.postorder()
        print(self.value)
root=Tree(5)
root.leftchild=Tree(2)
root.rightchild=Tree(7)
root.rightchild.rightchild=Tree(11)
root.rightchild.leftchild=Tree(10)
root.leftchild.rightchild=Tree(8)
root.leftchild.leftchild=Tree(3)
print("preorder")
root.preorder()
print("postorder")
root.postorder()
print("inorder")
root.inorder()