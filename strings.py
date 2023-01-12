##########################################################
#                       STRINGS
##########################################################
string = input()
print()

print(string.lower())
print(string.upper())
print(string.index("h"))
print(string.find("t"))
print(string.rstrip())
print(string.lstrip())
print(string.isalpha())
print(string.isalnum())
print(string.startswith("s"))
print(string.endswith("t"))
print(string.title())
print()

a = "Strings are used for storing text/characters"
b = a.split()
print(b)
c = "*".join(b)
print(c)
d = a.replace("are","too")
print(d)
print(c.count("*"))
print()

name = input()
age = input()

k = "{} is {} years old.".format(name,age)
print(k)