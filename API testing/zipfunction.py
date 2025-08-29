list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,22,33,44,55,66,77,88,99,100]

content=list(zip(list1,list2))
print(list(zip(*content)))


if 1 in list1 and 2 in list1:
    print("true")
