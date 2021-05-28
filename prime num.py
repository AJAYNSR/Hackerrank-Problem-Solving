'''prime no in a range'''

l = int(input("enter the lower limit:\n"))
u = int(input("enter the upper limit:\n"))
for n in range(l,u+1):
    if (n > 1):
        for i in range(2, n):
            if (n % i == 0):
                break
        else:
            print(n)

'''check a no is prime or not'''

 # n = int(input("enter the no. you want to check:\n"))
 # if(n>1):
 #     for i in range(2,n):
 #         if(n%i == 0):
 #             print(f"{n} is not a prime no.")
 #             break
 #     else:
 #         print(f"{n} is a prime no.")
 # else:
 #     print(f"{n} is a prime no.")

'''check a no is prime or not using sqrt func'''

# import math
# n = int(input("enter the no:\n"))
# if(n>1):
#     for i in range(2,int(math.sqrt(n)+1)):
#         if(n%i == 0):
#             print(f"{n} is not prime")
#             print(i)
#             break
#     else:
#         print(f"{n} is a prime no.")
#

