################################# LIST ###################################
list_file = [] #empty list

list_file.insert(0,5) #insert the element in specific index place
list_file.insert(1,10) #insert the element in specific index place
list_file.insert(0,6) #insert the element in specific index place
print(list_file)

list_file.remove(6) #remove an element
list_file.append(9) #adding element
list_file.append(1) #adding element 
list_file.sort(reverse=True) #descending order
print(list_file)

list_file.pop() #remove the last element
list_file.reverse() #reverse the all elements
print(list_file)

print(list_file.count(5)) #count the no.of 5 value elements in the list
print(list_file.index(10)) #find the elemets index number
print("_______________________________________________________")
print()
#########################################################################
# EXAMPLE PROGRAM 1
#########################################################################
''' Program Question 
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
'''

name = ["amazon","apple","facebook","google","leetcode"]
empty_list = []

for i in name:
    if ("l" in i) and ("e" in i):
        empty_list.append(i)

print(empty_list)
################################# END ###################################
