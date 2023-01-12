####################################################################################
#                       FUNCTION
####################################################################################
# Find the Odd or Even number
def even_odd(user_input):
    
    if user_input%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

print("Find the Odd or Even number.")
user_input = int(input("Enter Number : "))
even_odd(user_input)
print("_"*15)
print()

####################################################################################
# Write a Python function to find the Max of three numbers
def first_three_numbers(a):
    empty = []

    for i in a:
        i = int(i)
        empty.append(i)
    empty.sort(reverse=True)
    print(empty[:3])

print("Find first three max number.")
a = input("Enter Numbers : ").split()
first_three_numbers(a)
print("_"*50)
print()
####################################################################################
# repeated number removing from the list
def repeated_numbers(user):
    empty1 = []

    for i in user:
        count_no = user.count(i) == 1
        if count_no:
            empty1.append(int(i))
    return empty1

print("repeated number removing from the list")
user = input("Enter Numbers : ").split(" ")
result = repeated_numbers(user)
print(result)