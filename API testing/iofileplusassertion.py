import os
list=["Selenium", "Python","Java","C++"]


assert "Selenium" in list, "Validation failed"
print("Validation passed")

with open(os.getcwd() + "//demo.txt") as f:
     content=f.read()
     print(content)
     print(f.mode)
     print(f.name)
     assert not f.closed,"File is currently in open state"
     print("PASSED!")
     
     
print(f.closed)