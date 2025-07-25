"""Practice Dictionaries
I will write code to figure out how to create dictionaries.
Traverse through them.
Verify the mutability.
Try memeber functions
"""

ages = {"vish":30, "Harish": 20, "Phani K": 25, "Phani R": 16}
#Print the list

#Add new entries to the dictionary 
ages["Kesava"] = 100
ages ["Harshit"] = 40
print(f"the ages of the employees are {ages}")

#rewrite a value

ages["kesava"] = 120
ages ["Harshit"] = 200

#! Keys are case sensitive
 
print (ages)

#create empty dictionary and verify if it is empty 
new_dic = {}

if new_dic:
  print ("Dictionary is not empty")
else:
  print ("Dictionary is empty")

# Check the data type of the dictionary entry

print (f" the data type of the Ages dictionary is {type(ages)}")
#the above line prints the data type of the entire dictionary 

#Lets print the data type of the dictionary key
print (f"The data type of the dict key is {type(ages['Harshit'])}")

#removing an key value pair. It is like using del operator for lists 
print(ages)
del ages["kesava"]
print (ages)

# get(): used when the key is not existing.

print(ages.get("Kon", "His name does not exist"))
print(ages.get("vish", "His name does not exist"))

#Looping through dictionaries using items() function
for key, value in ages.items():
  print(f"Age of {key.upper()} is {value}")

#To just loop through the keys only use keys()

for key in ages.keys():
  print(f"{key} is present in the list")
