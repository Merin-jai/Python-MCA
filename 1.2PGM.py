# An electric power distribution company charges domestic customers as
# follows: Consumption unit Rate of charge:
# 1.2.1. 0-200 Rs. 0.50 per unit
# 1.2.2. 201-400 Rs. 0.65 per unit in excess of 200
# 1.2.3. 401-600 Rs 0.80 per unit excess of 400
# 1.2.4. 601 and above Rs 1.00per unit excess of 600
# 1.2.5. If the bill exceeds Rs. 400, then a surcharge of 15% will be charged,
# and the minimum bill should be Rs. 100/-
# Create a Python program based on the scenario mentioned above.
print("Enter the units consumed")
units=int(input())
if units <= 200:
    bill = units * 0.50
elif units >=201 and units <=400:
    bill=units*0.65
elif units >=401 and units >=600:
    bill=units*0.80
else:
    bill=units*1

if bill<100:
   bill=100
if bill>400:
    bill=bill*0.15+bill
print("BILL : ",bill)

