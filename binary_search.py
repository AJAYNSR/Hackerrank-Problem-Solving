from array import*

a = array('i',[])
n = int(input("enter the no. of elements:\n"))
for k in range(n):
    x = int(input("enter the elements:"))
    a.append(x)

# for i in range(n):
#     for j in range(i+1,n):
#         if(a[i]>a[j]):
#             temp,a[i],=a[i],a[j]
#             a[j]=temp
print(a)

search = int(input("enter the element to be searched:\n"))
l=0
u=n-1

while(l<=u):
    mid = (l + u) // 2
    if(a[mid] == search):
        print([mid+1])
        break
    elif(a[mid]<search):
        l = mid+1
    else:
        u = mid-1
if(l>u):
    print(f"{search} not found")


