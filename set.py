#########################################
#                 SET 
#########################################

a = {1,2,3,1,5,2,1}
b = {1,2,5,9,8,7,6}

#########################################
#               SET OPERATION
#########################################
print(a | b) #union
print(a & b) #intersection
print(a ^ b) #symmetric difference

print(a.isdisjoint(b)) #disjoint
print(a.issuperset(b)) #super set
print(a.issubset(b)) #sub set

#########################################
#               SET METHODS
#########################################
a.add("python") #add single elements
print(a)

c = a.copy() #copy
print(c)

a.pop() #remove 1st element
print(a)

a.update({"srikanth","python life"}) #add multiple elements
print(a)

a.remove("srikanth") #remove elements
print(a)

a.clear() #clear the set
print(a)
#########################################
#               FROZENSET
#########################################
d = frozenset(b)
print(d)

#########################################
#               END
#########################################