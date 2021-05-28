l = []
n = int(input("enter the no. of elements:\n"))
for i in range(n-1):
    l.append(int(input("enter the elements:")))
print(l)
count=0
for i in range(n-1):
    for j in range(n-1):
        if(l[i]==l[j]):
            count= count+1
if(count%2 == 1):
    print(l[i])

