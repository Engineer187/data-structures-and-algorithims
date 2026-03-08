l=[7,5,2,7,4,8,55,3,90,46]
#selection sort
run=True
a=0
"""
while run==True:
    b=l(a)
    c=l(a+1)
    if b>c:
        l(a)
"""
c=0
index=0
for i in range(len(l)):
    s=l[i]
    index=i
    for j in range(i+1,len(l)):
        r=l[j]
        if s>r:
            s=r
            index=j
    temp=l[i]
    l[i]=s
    l[index]=temp
    print(l)


