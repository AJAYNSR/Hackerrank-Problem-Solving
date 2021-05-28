from array import*

a = array('i',[])
n = int(input("enter the no of elements:"))
for i in range(n):
    x = int(input("enter the elements:"))
    a.append(x)
print(f"array:{a}")