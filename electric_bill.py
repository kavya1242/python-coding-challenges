# Program to calculate Electricity Bill based on units consumed
# Charges: First 50: ₹2/unit, 51-150: ₹3/unit, 151-250: ₹5/unit, Above 250: ₹8/unit
# Includes a 20% surcharge on the total bill

units = int(input())

# Initialize variables for different slabs
slab1_charge = 0
slab2_charge = 0
slab3_charge = 0
slab4_charge = 0

# Logic for Slab 1 (0 to 50 units)
if units > 0:
    s1_units = min(units, 50)
    slab1_charge = s1_units * 2

# Logic for Slab 2 (51 to 150 units)
if units > 50:
    s2_units = min(units - 50, 100)
    slab2_charge = s2_units * 3

# Logic for Slab 3 (151 to 250 units)
if units > 150:
    s3_units = min(units - 150, 100)
    slab3_charge = s3_units * 5

# Logic for Slab 4 (Above 250 units)
if units > 250:
    s4_units = units - 250
    slab4_charge = s4_units * 8

# Total Calculation
total_bill = slab1_charge + slab2_charge + slab3_charge + slab4_charge
surcharge = total_bill * 0.20
final_amount = total_bill + surcharge

if units == 0:
    print(0.0)
else:
    print("final amount",final_amount)