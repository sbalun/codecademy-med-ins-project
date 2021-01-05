# Python Dictionaries: Medical Insurance Project
# Scott Balun
# January 5, 2020
#
# Problem Statement: Create a program that organizes and updates medical records efficiently.
# Use your knowledge of Python dictionaries to create a database of medical records for patients.

# Create an empty dictionary called medical_costs
medical_costs = {}

# Populate our medical_costs dictionary by adding the following key-value pairs:
#  Add "Marina" to medical_costs as a key with a value of 6607.0.
#  Add "Vinay" to medical_costs as a key with a value of 3225.0.

medical_costs["Mariana"] = 6607.0
medical_costs["Vinay"] = 3225.0

# Using one line of code, add the following three patients to the medical_costs dictionary:
#  "Connie", with an insurance cost of 8886.0
#  "Isaac", with an insurance cost of 16444.0
#  "Valentina", with an insurance cost of 6420.0

medical_costs.update([('Connie', 8886.0), ('Isaac', 16444.0), ('Valentina', 6420.0)]) 

# Print medical_costs
print(medical_costs)

# Update the value associated with Vinay to 3325.0.  Print the updated dictionary.
medical_costs["Vinay"] = 3325.0
print(medical_costs)

# Create a variable called total_cost and set it equal to 0.  Iterate through the values in medical_costs and add each value to the total_cost variable.
# After the loop, create a variable called average_cost that stores the total_cost divided by the length of the medical_costs dictionary.
# Print average_cost with the following message:
#   Average Insurance Cost: {average_cost}

total_cost = 0
for key, value in medical_costs.items():
    total_cost += value

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: {}".format(str(average_cost)))

# Create two lists called names and ages with the following data:
#   names	    ages
#   Marina	    27
#   Vinay	    24
#   Connie	    43
#   Isaac	    35
#   Valentina	52

names = ['Marina','Vinay','Connie','Isaac','Valentina']
ages = [27,24,43,35,52]

# Create a variable called zipped_ages that is a zipped list of pairs between the names list and the ages list.


