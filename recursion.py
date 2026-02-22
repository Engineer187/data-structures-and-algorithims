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



def sum(n):
    if n == 1:
        return n
    else:
        return n+sum(n-1)
a=sum(10)
print(a)




def multiple(n):
    if n == 1:
        return n
    else:
        return n*multiple(n-1)
a=multiple(10)
print(a)