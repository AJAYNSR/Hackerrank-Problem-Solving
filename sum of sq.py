n = int(input("enter the no of terms:\n"))
sum=0
for i in range(1,n+1):
    sum = sum + i**3
print("sum of first",n ,"natural nos. is",sum)