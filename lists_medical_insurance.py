# Codecademy Homework Project :: Python Lists medical insurance project
# Editor and Author: Scott Balun
# December 22, 2020

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = zip(names,insurance_costs)

estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

# Additional Practice
# Calculate the diff between the actual ins cost data and the estimated ins cost
ins_cost_diff = []
maria_ins_cost_diff = abs(estimated_insurance_data[0][1] - insurance_costs[0])
ins_cost_diff.append(("Maria", maria_ins_cost_diff))

rohan_ins_cost_diff = abs(estimated_insurance_data[1][1] - insurance_costs[1])
ins_cost_diff.append(("Rohan", rohan_ins_cost_diff))

valentina_ins_cost_diff = abs(estimated_insurance_data[2][1] - insurance_costs[2])
ins_cost_diff.append(("Valentina", valentina_ins_cost_diff))

print(ins_cost_diff)

# Estimate the insurance cost for a new individual
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)

# append his name to names and his actual insurance cost, 2930.0, to insurance_costs
names.append("Akira")
insurance_costs.append(2930.0)

print(names)
print(insurance_costs)