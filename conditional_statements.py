# if conditional statements
##############################################################
# Example program 1
##############################################################
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print()

if age >= 18:
    print(name + " eligible for vote.")
else:
    print(name + " not eligible for vote.")
print("_________________________________________________")
print()

##############################################################
# Example program 2
##############################################################

marks = int(input("Enter student marks: "))

if marks >= 35 and marks <= 49:
    print("C Grade")
elif marks >= 50 and marks <= 59:
    print("C+ Grade")
elif marks >= 60 and marks <= 69:
    print("B Grade")
elif marks >= 70 and marks <= 79:
    print("B+ Grade")
elif marks >= 80 and marks <= 89:
    print("A Grade")
elif marks >= 90:
    print("A+ Grade")
else:
    print("FAIL")