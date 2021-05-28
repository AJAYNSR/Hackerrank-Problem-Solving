l = int(input("lower limit:\n"))
u = int(input("upper limit:\n"))
for n in range(l,u+1):
    order = len(str(n))
    sum = 0
    te = n
    while(te>0):
        rem = te % 10
        sum = sum + pow(rem,order)
        te = te/10
    if(n==sum):
        print(n, end=" ")
