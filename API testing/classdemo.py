class geteven:
    def __init__(self):
        print("IT IS GETEVEN CLASS")
    
    def evennumber(self,num):
        if num%2==0:
            print("it is even number")
        else:
            pass
    def bubye(self):
        print("bye from base class")


class getevenlist(geteven):
    def __init__(self,satz):
        self.satz=satz
        print("IT IS GETEVENLIST CLASS" + satz)
    
    def even_odd_list(self,numm):
       super().bubye() 
       even_num_list=[]
       odd_num_list=[]
       for c in numm:       
           if c%2==0:
              even_num_list.append(c)
           else:
              odd_num_list.append(c)
       print(even_num_list)
       print("******************")
       print("\n")
       print(odd_num_list)
        

x=geteven()
x.evennumber(2)
listt=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y=getevenlist("hello")
y.even_odd_list(listt)
y.evennumber(44)


xy=set({1,2,4,6,7,8})
for c in xy:
    if c ==2:
        print(c)
print(xy)


sent=str("Welcome to the world")
print(sent)

for s in sent:
    if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
        print(s + " is a vowel")
        
for s in ["a","e","i","o","u"]:
    if sent.__contains__(s):
        print("contains vowel")
        break

try:
    content=open("/Users/aamiraliraza/Desktop/python automation testing/API testing/demo.txt","r")
    print(content.write("WHAT?"))
except FileNotFoundError as err:
    print("Something went wrong ", err)
except Exception as err:
    print("Another exception ", err)
    
    

try: 
    a=int(input("Enter A "))
    b=int(input("Enter B "))
    sum=a/b
    print("Total: ", sum)
except TypeError as err:
    print("The error is: ", err)
except ZeroDivisionError as err:
    print("The error is: ", err)
except Exception as err:
    print("Unknown exception: ", err)
finally:
    print("Have a nice day")