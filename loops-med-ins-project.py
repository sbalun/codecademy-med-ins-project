#
# Python Loops: Medical Insurance Project

# Problem: You are interested in analyzing medical insurance 
# cost data efficiently without writing repetitive code.
#
# Take a look at the follwoing three lists:
#
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
# stores the names of seven individuals.

estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
 # stores the estimated medical insurance costs for the individuals.

actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]
 # stores the actual insurance costs paid by the individuals.

# We want to calculate the average insurance cost each person paid. 
# We’ll start by adding up all of the insurance costs.
total_cost = 0

# Use a for loop to iterate through actual_insurance_costs and 
# add each insurance cost to the variable total_cost.

for cost in actual_insurance_costs:
    total_cost += cost

# Create a variable called average_cost that stores the 
# total_cost divided by the length of the actual_insurance_costs list.

average_cost = total_cost / len(actual_insurance_costs)

# Print average_cost with the following message: Average Insurance Cost: <average_cost> dollars.

print("Average Insurance Cost: " + average_cost + " dollars.")

