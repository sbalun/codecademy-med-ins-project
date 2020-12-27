# Python Loops: Medical Insurance Project
#
# Problem: You are interested in analyzing medical insurance cost data efficiently without writing repetitive code.
#
# Take a look at the following three lists:
#
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
# stores the names of seven individuals.

estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
 # stores the estimated medical insurance costs for the individuals.

actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]
 # stores the actual insurance costs paid by the individuals.

# We want to calculate the average insurance cost each person paid. We’ll start by adding up all of the insurance costs.
total_cost = 0

# Use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost.
for cost in actual_insurance_costs:
    total_cost += cost

# Create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.
average_cost = total_cost / len(actual_insurance_costs)

# Print average_cost with the following message: Average Insurance Cost: <average_cost> dollars.
print("Average Insurance Cost: $" + str(average_cost) + "0 dollars.")

# For each individual in names, we want to determine whether their insurance cost is above or below average.
# Write a for loop with variable i that goes from 0 to len(names).  Inside of the for loop, do the following:
# - Create a variable name, which stores names[i].
# - Create a variable insurance_cost, which stores actual_insurance_costs[i].
# - Print out the insurance cost for each individual, with the following message:
# - The insurance cost for <name> is <insurance_cost> dollars.

for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print("\nThe insurance cost for " + name + " is $" + str(insurance_cost) + "0 dollars.")

# Inside of the for loop, use if, elif, else statements after the print statement to check whether the insurance 
# cost is above, below, or equal to the average. Print out messages for each case:
# - When insurance_cost is higher than the average, print out the following: The insurance cost for <name> is above average.
# - When insurance_cost is lower than the average, print out the following: The insurance cost for <name> is below average.
# - Otherwise, print out the following: The insurance cost for <name> is equal to the average.
    
    if insurance_cost > average_cost:
        print("The insurance cost for " + name + " is above the average.")
    elif insurance_cost < average_cost:
        print("The insurance cost for " + name + " is below the average.")
    else:
        print("The insurance cost for " + name + " is equal to the average.")

# If you look closely at actual_insurance_costs and estimated_insurance_costs, you will
# notice that each of the actual insurance costs are 10% higher than the estimated insurance costs. 
# 
# Using a list comprehension, create a new list called updated_estimated_costs, 
# which has each element in estimated_insurance_costs multiplied by 11/10.

updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

# Print updated_estimated_costs. You should see that the list now looks the same as actual_insurance_costs.
print(updated_estimated_costs)




