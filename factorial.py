
n = int(input("enter the no.\n"))
fact=1
if(n==1 or n==0):
    print("factorial",fact)
elif(n<0):
    "enter a positive integer"
else:
    for i in range(n):
        fact = fact*n
        n=n-1

    print("factorial of {} is:".format(n),fact)