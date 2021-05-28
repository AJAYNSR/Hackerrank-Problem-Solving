from array import*

a = array('i',[])
n = int(input("enter the no. of elements:\n"))
for k in range(n):
    x = int(input("enter the elements:"))
    a.append(x)
search = int(input("enter the element to be searched:"))
for i in range(n):
    if(a[i] == search):
        print(i+1)
        break
else:
    print(-1)