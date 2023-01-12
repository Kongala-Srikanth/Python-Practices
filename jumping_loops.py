# Jumping statements
###########################################################################
# Break statements
###########################################################################
string = "SRIKANTH"

for i in string:
    if i == "K": # chenk the if condition i is matching to the k or not
        break   # when k is find the stop the iteration
    print(i,end=" ")


###########################################################################
# Continue
###########################################################################
# Removing all spaces
print()
print("____________________________________________________")
statement = input()
print()

for i in statement:
    if i == " ":
        continue
    print(i,end=" ")


###########################################################################
# Pass
###########################################################################

if True:
    pass