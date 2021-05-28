'''2 GP in a series
series - 1 1 3 2 4 9 8 27 16 81 32 243......upto n'''

# n = int(input("enter the n-th term:"))
# a,b = 1,1
# for i in range(2,n+1):
#     if(i%2 == 0):
#         a = a*2
#     else:
#         b = b*3
# if(n%2 != 0):
#     print(f"the value of {n} is {a}")
# else:
#     print(f"the value of {n} is {b}")
#
# '''0 0 2 1 4 2 6 3 8 4 10 5 12 6......'''
#
# n = int(input("enter the n-th term:"))
# a,b = 0,0
# for i in range(2,n+1):
#     if(i%2 == 0):
#         a = a+2
#     else:
#         b = b+1
# if(n%2 != 0):
#     print(f"odd term{n} = {a}")
# else:
#     print(f"even term{n} = {b}")

'''series - 1 2 1 3 2 5 3 7 5 11 8 13......
odd is fibonacci and even is prime nos.'''

n = int(input("enter the n-th term:"))
a=1
b=1
c=0
count=1
for i in range(2,n+1):
    if(i%2 != 0):
        c = a + b
        a = b
        b = c

    else:
        for j in range(1,n+1):
            flag=0
            for k in range(2,j):
                if(j%k == 0):
                    flag = 1
                    break
            if(flag == 0):
                count = count+1
                # if(count == n):
                #     print(j)
                #     break
                # j = j+1


if(n%2 != 0):
    print(f"{n}th term is {a}")
else:
    print(f"{n}th term is {count}")

