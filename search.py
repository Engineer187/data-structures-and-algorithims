#liner search
list=[1,6,4,2,6,8,4,9,26,4,8]
a=int(input("number :"))
value=False
for i in range(0,len(list),1):
    if a==list[i]:
        value=True
        break
if value==True:
    print("number is found")
if value==False:
    print("number is not found")

#binary search
val=False
l=[12,22,32,42,52,62,72,82,92]
b=int(input("number :"))
start=0
end=len(l)-1
while start<=end:
    mid=(start+end)//2
    if b==l[mid]:
        val=True
        break
    elif b<l[mid]:
        end=mid-1
    elif b>l[mid]:
        start=mid+1
if val==True:
    print("number is found")
if val==False:
    print("number is not found")