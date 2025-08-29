print("hello world")


#arrays
#browsers = ["safari", "chrome", "firefox", "opera", "IE"]
#print(browsers[0:5])
#for browser in browsers:
#    print(browser)
#dictionary

configs = {
    "browser":"chrome",
    "test":"automation",
    "lang":"python",
    "OS":"windows"
}
def getValues(dic,*key):
    return [dic.get(k) for k in key]
#for conf in configs.values():
#   print(conf)
print(getValues(configs, "browser","test"))


if "browser" in configs:
    print("exist")
    
myset=set({"aamir","65","43"});
print(type(myset))
myset.add("33")
myset1 = {"aamir1, aamir2, aamir3"}
print(type(myset1))
print(myset)
myset.pop()


for set in myset:
    if "33" in set:
        print("exists")
    
myset.discard("aamir")
print(myset)