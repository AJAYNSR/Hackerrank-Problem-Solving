#a = int(input("enter the first no.:\n"))
#b = int(input("enter the second no.:\n"))
#sum = a+b
#print("sum of {0} and {1} =".format(a,b),sum)

n = int(input("enter the no of terms:\n"))

if(n<0):
    print("enter a postive integer")

else:
    sum = (n*(n+1))/2

    print("sum of",n, "terms is:",sum )