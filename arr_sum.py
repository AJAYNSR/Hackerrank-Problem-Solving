from array import*
sum = 0
a = array('i',[])
n = int(input("enter the no of elements:"))
for i in range(n):
    x = int(input("enter the elements:"))

    a.append(x)

for j in range(0,n,1):
    sum=sum + a[j]
print(a)
print(sum)