dic = {"name":"aamir", "age":28, "prof": "QA"}
print(dic.get("name"))
dic1 = {"frontend":["Karl","Mike","Sabine"],"backend": ["Susan","Fabian","Steve"]}
print(dic1)
front = dic1.get("frontend")
back = dic1.get("backend")
for f in front,back:
    print(f)
dic1.pop("frontend")
print(dic1)
print(dic1)

