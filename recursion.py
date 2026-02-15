b=0
def name(a,n):
    if n == 0:
        return
    else:
        print(a)
        name(a,n-1)
a=input("name?")
name(a,6)



def num(n):
    if n == 0:
        return
    else:
        num(n-1)
        print(n)
a=input("num?")
num(10)