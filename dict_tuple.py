######################################################################
#                           DICTIONARY
######################################################################
print("DICTIONARY")
print()
py_dict = {"name":"srikanth","age":23,"skills":["python","html","css"]}
print(py_dict)
print(py_dict["skills"]) #only key is access
print(py_dict.get("name")) #only key is access
print(py_dict.keys()) #all key in dict
print(py_dict.values()) #all values in dict
print(py_dict.items()) #all key and values in dict

d = py_dict.copy() #duplicate dict
py_dict.update({"inter":"python life","age":22}) #updated dcit values and added
print(py_dict)
print(d)
d.clear() #delete all elements in dict
print(d)
py_dict.pop("name") #remove selected elements
print(py_dict)

for k,v in py_dict.items():
    print(k,v)
print('_______________________________________________________')

######################################################################
#                           TUPLE
######################################################################
print("TUPLE")
d = input("Enter 1st input: ").split()
d2 = input("Enter 2nd input: ").split()
t = tuple(d)
t2 = tuple(d2)
print(t)
print(t2)

add = t + t2
print(add)

print(t*5)

print(t is t2)
print("55" in t or "1" in t2)

######################################################################
#                           END
######################################################################