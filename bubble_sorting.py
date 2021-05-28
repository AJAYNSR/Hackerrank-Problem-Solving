from array import*
a = array('i',[])
n = int(input("enter the no. of elements:"))
for k in range(n):
    x = int(input("enter the values:"))
    a.append(x)
print("the unsorted array is:",a)

'''logic'''

for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("the sorted array:",a)