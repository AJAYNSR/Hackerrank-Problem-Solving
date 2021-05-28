from array import*

a = array('i',[])
n = int(input("enter the no. of elements:\n"))
for k in range(n):
    x = int(input("enter the elements:"))
    a.append(x)
print("the unsorted array is:",a)

'''logic'''

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if(a[min]>a[j]):
            min = j
    temp =  a[i]
    a[i] = a[min]
    a[min] = temp
print("the sorted array :",a)
for y in (a):
    print(y)
