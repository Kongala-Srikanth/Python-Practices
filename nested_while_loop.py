# Nested while loop
######################################################

n = int(input("Enter the number: "))
print()

while n > 0:
    while n > 0:
        print("* "*n)
        n -= 1

######################################################
# Nested for loop
######################################################

number = int(input("Enter the number: "))

for i in range(number):
    for j in range(i):
        print("* ",end=" ")
    print()

################### END ###############################