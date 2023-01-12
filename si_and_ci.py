'''
Example #1
Consider a person XYZ who keeps $ 1000 in a bank for one year at a 5% interest rate.
 Calculate the Simple and compound interest (compounded annually).
'''
#######################################################################################
# Simple Interest = P * R * T/100

P = float(input("Principal Amount: "))
R = float(input("Annual Interest Rate: "))
T = int(input("Time In Years: "))

si = P * R * T/100
si = str(si)
print("Simple Interest = " + si)

#######################################################################################
# Compound Interest = P (1 + r/100)T – P

ci = P*(1 + R/100)**T-P
ci = str(ci)
print("Compound Interest = " + ci)
print("_____________________________________________")
print()
##################################### END #############################################