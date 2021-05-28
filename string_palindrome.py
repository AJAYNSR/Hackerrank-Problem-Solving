n = int(input("enter the no.:\n"))
temp = n
sum = 0
while(n!=0):
    rem = n % 10
    sum = (sum*10) + rem
    n = n//10
if(temp==sum):
    print("no is palindrome")
else:
    print("no is not!")

n = input("enter string:\n")
if(n==n[::-1]):
    print("the string is palindrome")
else:
    print("not palindrome!")

n = input("string:\n")
n = n[::-1]
print("reversed string is",n)