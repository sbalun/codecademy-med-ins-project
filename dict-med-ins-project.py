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
print("\n", medical_costs)

# Create a variable called total_cost and set it equal to 0.  Iterate through the values in medical_costs and add each value to the total_cost variable.
# After the loop, create a variable called average_cost that stores the total_cost divided by the length of the medical_costs dictionary.
# Print average_cost with the following message:
#   Average Insurance Cost: {average_cost}

total_cost = 0
for key, value in medical_costs.items():
    total_cost += value

average_cost = total_cost / len(medical_costs)
print("\nAverage Insurance Cost: {}".format(str(average_cost)))

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
zipped_ages = zip(names,ages)

# Create a dictionary called names_to_ages by using a list comprehension that iterates through
# zipped_ages and turns each pair into a key : value item.  Print names_to_ages to see the result.

names_to_ages = {names: ages for (names, ages) in zipped_ages}
print("\nThe values in the dict, names_to_ages, are: ", names_to_ages)

# Use .get() to get the value of Marina’s age and store it in a variable called marina_age. 
# Use None as a default value if the key doesn’t exist. 
# Print marina_age with the following message: 'Marina's age is {marina_age}'
mariana_age  = names_to_ages['Marina']
print("\nMarina's age is {}".format(mariana_age))

# Create an empty dictionary called medical_records
medical_records = {}

# Add "Marina" to medical_records as a key with the value being a dictionary of medical data:
# {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

# Add the following individuals:
#
# Name	    Age	Sex	    BMI	    Children	Smoker	    Insurance Cost
# Vinay	    24	Male	26.9	0	        Non-smoker	3225.0
# Connie	43	Female	25.3	3	        Non-smoker	8886.0
# Isaac	    35	Male	20.6	4	        Smoker	    16444.0
# Valentina	52	Female	18.7	1	        Non-smoker	6420.0

medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age":43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age":52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0} 

# Print medical_records to see the result
print("\n", medical_records)

# The medical_records dictionary acts like a database of medical records. Let’s access a specific piece of data in medical_records.
# Print out Connie’s insurance cost with the following message: "Connie's insurance cost is X dollars."
print("\nConnie's insurance cost is ${}0 dollars.\n".format(medical_records["Connie"]["Insurance_cost"]))

# Remove Vinay from medical_records.
medical_records.pop("Vinay")

# Use a for loop to iterate through the items of medical_records. 
# For each key-value pair, print out a string that looks like the following:
#   {Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}

for key, value in medical_records.items():
    #print(key,value['Age'])
    print("{} is a {} year old {} {} with a BMI of {} and a insurance cost of ${}0".format(key, value['Age'], value['Sex'], value['Smoker'], value['BMI'], value['Insurance_cost']))

print("\n--------------------- EXTRA CREDIT ---------------------")
# Extra Credit: Create a function called update_medical_records() that takes in the name of an individual
# as well as their medical data, and then updates the medical_records dictionary accordingly.

def update_medical_records(name, age=-1, sex="", smoker="", bmi=-1, ins_cost=-1):
    if age > -1:
        medical_records[name]["Age"] = age
    if sex != "":
        medical_records[name]["Sex"] = sex
    if smoker != "":
        medical_records[name]["Smoker"] = smoker
    if bmi > -1:
        medical_records[name]["BMI"] = bmi
    if ins_cost > -1:
        medical_records[name]["Insurance_cost"] = ins_cost

# Update Marina's bmi to 45
update_medical_records("Marina", bmi=45)

print("Marina's updated bmi should be 45: {}".format(medical_records["Marina"]["BMI"]))