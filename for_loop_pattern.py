###########################################################
# for loop star pattern programs
###########################################################

no_of_stars = int(input("Number of Starts: "))

for i in range(1,no_of_stars+1):
    print("* "*i)
print()

###########################################################

for i in range(1,no_of_stars+1):
    print("* " * no_of_stars)
print()

###########################################################
j = no_of_stars-2

for i in range(1,no_of_stars+1):
    print(" "*j + "* "*i)
    j -=1
print()

###########################################################
j = no_of_stars

for i in range(1,no_of_stars+1):
    print(" "*(i-1) + "* "*j)
    j -= 1
print()

###########################################################
j = no_of_stars

for i in range(1,no_of_stars+1):
    print("* "*j + " "*(i-1))
    j -= 1

########################### END #############################