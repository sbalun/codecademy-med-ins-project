# Python Strings - Medical Insurance Project
#
# The string medical_data stores the medical records for ten individuals. Each record is separated by a ; 
# and contains the name, age, BMI (body mass index), and insurance cost for an individual, in that order.

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Print medical_data to see the output in the terminal
print(medical_data + '\n')

# Replace all instances of # in medical_data with $. Store the result in a variable called updated_medical_data.
updated_medical_data = medical_data.replace("#","$")

print(updated_medical_data)

num_records = 0

for character in updated_medical_data:
  if character == "$":
    num_records += 1

# Outside of the loop, print num_records with the following message:
print("There are {} medical records in the data.".format(num_records))

# Split the updated_medical_data string into a list of each medical record. 
# Remember that each medical record is separated by a ; in the string. 
# Store the result in a variable called medical_data_split and print this variable.
 
updated_medical_split = updated_medical_data.split(";")
print(updated_medical_split, "\n")

# Split each medical record into its own list. First, define an empty list called medical_records
medical_records = []

# Iterate through medical_data_split and for each record, split the string after each comma (,) 
# and append the split string to medical_records.  Print medical_records after the loop

for records in updated_medical_split:
    medical_records.append(records.split(","))

print(medical_records)

# Create an empty list called medical_records_clean
medical_records_clean = []

# Use a for loop to iterate through medical_records. Inside of the loop, create an empty list 
# called record_clean. We’ll use this list to store a formatted version of each medical record
# After the record_clean variable, create a nested for loop that goes through each record:
# Inside of this loop, append item.strip() to record_clean to remove any whitespace from the string.
#
# Add each cleaned up record to medical_records_clean. Outside of the nested for loop, 
# append record_clean to medical_records_clean

for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

# Print medical_records_clean outside of the for loops to see the output.
print(medical_records_clean, '\n')

# Print out the names of each of the ten individuals
# Update records before the print statement so that all of the characters are uppercase.

for record in medical_records_clean:
  print(record[0].upper())

# Create four empty lists to store name, age, bmi, insurance_cost
names = []
ages = []
bmis = []
insurance_costs = []

# iterate through medical_records_clean and for each record:
#   Append the name to names.
#   Append the age to ages.
#   Append the BMI to bmis.
#   Append the insurance cost to insurance_costs.

for item in medical_records_clean:
    names.append(item[0])
    ages.append(item[1])
    bmis.append(item[2])
    insurance_costs.append(item[3])

# Print names, ages, bmis, and insurance_costs outside of the loop.
print(names, ages, bmis, insurance_costs)

# Calculate the average BMI in our dataset.
# Create a variable called total_bmi and set it equal to 0.
total_bmi = 0

# Use a for loop to iterate through bmis and add each bmi to total_bmi.  Convert bmi to a float
