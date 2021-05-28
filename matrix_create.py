from numpy import*
matrix = []
row = int(input("enter the no. of rows:"))
col = int(input("enter the no. of columns:"))
for i in range(row):
    a = []
    for j in range(col):
        x = int(input("enter the elements:\n"))
        a.append(x)
    matrix.append(a)
print(matrix)
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()