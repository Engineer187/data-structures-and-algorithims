from stack import Stack
stack=Stack(10)
a=input("expesion")
openingbracets=["(","{","["]
closingbracets=[")","}","]"]
for i in a:
    if i in openingbracets:
        stack.push(i)
    if i in closingbracets:
        index=closingbracets.index(i)
        a=openingbracets[index]
        if len(stack.list)>0:
            if stack.peek()==a:
                stack.pop()
if len(stack.list)==0:
    print("brackets is balanced")
else:
    print("not balenced")