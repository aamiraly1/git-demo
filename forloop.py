t1=(1,2,3)
t2=(10,20,30)
t3=(100,200,300)
l1=[t1,t2,t3]

for a,b,c in l1:
    print(a)
    print(b)
    print(c)
    
d=dict({1:"Selenium",2:"Cypress",3:"Appium",4:"Jenkins"})

for x in d.items():
    print(x)

#l2=["1","2","3","4","5","6","7","8","9","10"]
#feedback=""
#while feedback not in l2:
#    feedback=input("please enter feedback")
#    print("thank you ")



def check_even_number(list1):
    even_list=[]
    odd_list=[]
    for l in list1:
        if l%2==0:
            even_list.append(l)
        else:
            odd_list.append(l)
    return even_list, odd_list
            
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
result1,result2=check_even_number(list1)
print(result1)
print(result2)
def print_names(**kwargs):
    for name in kwargs.items():
        print(name)
print_names(namee="hello",age="world",sex="bye")