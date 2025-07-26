"""Further adventures in Dictionaries"""
#values 
ages = {"vish":30, "Harish": 20, "Phani K": 25, "Phani R": 16}
print(ages.values())
print (ages.keys())
#Value(), keys() returns lists. I will explore if they can be assigned to lists

key_list = ages.keys()
value_list = ages.values()

print(f"The keys are here:{key_list}")
print(f"The values are here:{value_list}")

####let me practice iterator one more time 

for keys, values in ages.items():
  print(f"The {keys} age is {values}")

# I want to try the set() function. Set() can be used around keys() and values()
#to print uniques elements

set_test = {"Harish":50, "vish":50, "Vish":55, "Ravi": 60, "Gopala": 65, "Gopala": 70}
print (set(set_test.keys()))
#print(set(f"Unique keys are {set_test.values()}"))

""" Nesting of Dictionaries"""
##List of dictionaries 

marks = {"Harish": 100, "vish":65, "Vish":35, "Ravi": 90, "Gopala": 60, "Gopala": 70}
fav_subjects = {"Harish": "Biology", "vish": "Maths", "Vish": "Computers", "Ravi":"Networking", "Gopala": "cloud", "Gopala": "Kubernetes"}
skill_matrix = [marks, fav_subjects]
print(skill_matrix)
print (type(skill_matrix))

#for each key in marks find what is the associated favorite subject
for key in marks.keys():
  if key in fav_subjects:
    print(f"{key} favorite subject is {fav_subjects[key]} and the marks are {marks[key]}") 
x