"""Lists in dictionar"""

"""Further adventures in Dictionaries"""

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
    
###Dictionaries having lists 
my_dict = {"Name":"Harish", "Subjects": ["Sci", "His", "Eng", "Tel"], "Age" : 45]

#I will traverse through the dictionary 
for keys, values in my_dict.values():
    if not isinstance(values,List):
        print (values):
    else:
        for iterate in values:
            print (values[iterate])
 