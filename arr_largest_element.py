from array import*

a = array('i',[])
n = int(input("enter the no of elements:"))
for i in range(n):
    x = int(input("enter the elements:"))
    a.append(x)
print("array:",a)
'''largest element in an array'''
max = a[0]
for j in range(1,n):
    if(a[j]>max):
        max = a[j]

print("largest element:",max)

