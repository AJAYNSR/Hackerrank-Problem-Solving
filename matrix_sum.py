from numpy import*

 m1 = []
n = int(input("enter the size of matrix(N*N):"))
 for i in range(n):
     a = []
     for j in range(n):
         a.append(int(input("enter the elements:")))
     m1.append(a)
 print("m1:",m1)

 m2 = []
 for i in range(n):
     a = []
     for j in range(n):
         a.append(int(input("enter the elements:")))
     m2.append(a)
 print("m2:",m2)

 res = []
 for i in range(n):
     a = []
     for j in range(n):
         a.append(m1[i][j] + m2[i][j])
     res.append(a)
 print("sum of array:",res)
'''array with all elements 0'''

result =[[0 for j in range(n)]for i in range(n)]
print(result)
 for i in range(n):
     for j in range(n):
         result[i][j] = m1[i][j]+m2[i][j]
 print("result:",result)

