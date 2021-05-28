from array import*

a = array('i',[])
n = int(input("enter the no of elements:"))
for k in range(n):
    x = int(input("enter the elements:"))
    a.append(x)
    '''slicing of array'''
# k = int(input("slices position:"))
# b = a[0:k]
# a1 =a[k::]+b[::]
# print("sliced array:",b)
# print(a1)
mul = 1
num = int(input('enter any no.\n'))
for i in range(n):
    mul = mul*a[i]
rem = mul%num
print(f"reminder:{rem}")
