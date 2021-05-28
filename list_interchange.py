# l1 = [21,51,52,41,57,52]
# size = len(l1)
# temp = l1[0]
# l1[0] = l1[size-1]
# l1[size-1] = temp
# print("list:",l1)
# for i in l1:
#     print(i)
'''user input'''
# list = []
# n = int(input("length:"))
#
# for i in range(n):
#     x = int(input("enter the elements:"))
#     list.append(x)
# print(list)
'''remove the nth occurance of a word'''

lis = ["check","and","remove","the","occurance","of","the","word","which","occured","repeatedly","remove","the","last","occurance","of","the","word"]
word = input("enter the word to check:\n")
n = int(input("N-th word to be removed:"))
new_list = []
flag = 0
for i in range(len(lis)):
    if(lis[i] == word):
        flag = flag+1
        if(flag!=n):
            new_list.append(lis[i])
    else:
        new_list.append(lis[i])
lst = new_list
if(flag==0):
    print(f"{word} not found")
else:
    print("new list is:",lst)



