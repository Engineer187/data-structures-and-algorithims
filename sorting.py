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
#buble sort
l2=[5,2,7,9,1,6,3,4,10,8]
for x in range (len(l2)):
    for y in range (len(l2)-x-1):
        v1=l2[y]
        v2=l2[y+1]
        if v1>v2:
            temp1=l2[y]
            l2[y]=l2[y+1]
            l2[y+1]=temp1
    print(l2)
#sincoserion sort
l3=[5,2,7,9,1,6,3,4,10,8]
"""
l4=[1]
m=l3[0]
print(m)
l4[0]=m
for i in range (len(l3)-1):
    m=l3[i+1]
    for x in range(len(l4)):
        c=l4[x]
        if c<m:
            l4[x-1]=m
print(l4)
"""
print("insersion sort")
for i in range(1,len(l3)):
    key=l3[i]
    j=i-1
    while j>=0 and key<l3[j]:
        l3[j+1]=l3[j]
        j=j-1
    l3[j+1]=key
    print(l3)