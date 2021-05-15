# Creating medical records using dictionaries:
medical_costs = {}

#Adding data to the dictionary:
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

#Updating Vinay's insurance cost:
medical_costs["Vinay"] = 3325.0

#Calculating average medical cost of each patient:
total_cost = 0
for x in medical_costs.values():
  total_cost += x

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

#Lists of names and ages to add to the dictionary:
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

#Creating the dictionary using list comprehension:
zipped_ages = zip(names, ages)
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

#Example of how to get the value of someone's age:
marina_age = names_to_ages.get("Marina", "None")
print("Marina's age is " + str(marina_age))

#Creating a dictionary to represent a database of medical records that cointains info such as name, age, bmi, etc.:
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

#Example of how to access a specific piece of data in the dict medical_records:
Isaac = medical_records["Isaac"]["BMI"]
print(Isaac)
print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

#Deleting Vinay's info in the database:
medical_records.pop("Vinay")

#Taking a closer look at each's patient medical record:
for key, value in medical_records.items():
  print(key + " is a " + str(value["Age"]) + \
  " year old " + value["Sex"] + " " + value["Smoker"] \
  + " with a BMI of " + str(value["BMI"]) + \
  " and insurance cost of " + str(value["Insurance_cost"]))

