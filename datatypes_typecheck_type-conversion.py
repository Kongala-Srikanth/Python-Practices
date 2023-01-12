# Data Types Type checking
######################################################
# DATA TYPES
######################################################
name = "SRIKANTH"      # String
age = 23               # Integer
gpa = 7.0              # Float
complex_value = 2 + 3j #Complex
print(name,age,gpa,complex_value)
print()

######################################################
# TYPE CHECKING
######################################################
print(type(name))
print(type(age))
print(type(gpa))
print(type(complex_value))
print()

######################################################
# TYPE CONVERSION
######################################################
# Implicit // Without lossing data
a = 10
int_to_float = float(a)
print(int_to_float)
print(type(a))
print(type(int_to_float))
print()

######################################################
# Explicit // Data loss
a = 10.5
float_to_int = int(a)
print(float_to_int)
print(type(a))
print(type(float_to_int))
print()

######################################################
'''
TYPE CONVERSION
int -----> float// YES
float -----> int// YES
int -----> str// YES
float -----> str// YES
str_int_number -----> int// YES
str_int_number -----> float// NO
str_float_number -----> int // NO
str_float_number -----> float// YES
'''