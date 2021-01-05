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
print(medical_data)

# Replace all instances of # in medical_data with $. Store the result in a variable called updated_medical_data.
updated_medical_data = medical_data.replace("#","$")

print(updated_medical_data)

