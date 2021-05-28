from array import*

a = array('i',[])
n = int(input("enter the no. of elements:\n"))
for k in range(n):
    x = int(input("enter the elements:"))
    a.append(x)
print("the unsorted array is:",a)

'''logic'''

for i in range(1,n):
    temp = a[i]
    j=i-1
    while(j>=0 and a[j]>temp):
        a[j+1] = a[j]
        j=j-1
    a[j+1] = temp
print("the sorted array:",a)
for k in range(n):
    print(a[k])
