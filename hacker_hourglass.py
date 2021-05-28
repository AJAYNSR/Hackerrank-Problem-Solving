lst = []
n = int(input("enter the no. of rows and columns:"))
for i in range(n):
    lst.append(list(map(int,input("enter the elements:").rstrip().split())))
print(lst)