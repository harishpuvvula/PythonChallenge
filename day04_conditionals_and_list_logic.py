#!/usr/bin/env python
# coding: utf-8

# In[21]:


"""Will test the if conditional statements
"""
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print (car.upper())
    else:
        print(car.lower())
#Testing for equality is case sensitive in Python 
car = "Audi"
if car == "audi":
    print ("the case matched")
else:
    print ("case mismatch, check your case")

#checking inequality with != operator

for car in cars:
    if car.lower() != "bmw":
        print("it is not a bmw")
    else:
        print ("It is a BMW!")
#checking if the value is in the list using "in" operator 

if "bMw" in cars: #the case is a mismatch
    print ("bmw is in the list dont add")
else:
    print ("bmw is not in the list")

#this code asks the user to enter a car name if the car exists in the list, it is skipped, else it adds
car_name = input(print("Please enter a car name"))
if car_name not in cars:
    print("the car is not in the list. Let me add it ")
    cars.append(car_name)
else:
    print ("the car is already on the list")

print (cars)

#Let me toy with Boolean 
flags= isinstance(car, str)
print (flags)


""" verify if...elif ...else
prompt for age and verify the range of age and mention the education one has to take"""

age = int(input(print("Enter your age so that I can specify the education you need to pursue")))

if age < 3:
    print ("You are such a baby: have fun while it lasts")
elif age > 3 and age <= 5:
    print ("Time to learn a few household items and colors. Just so you stay entertained")
elif age > 5 and age < 7:
    print ("Time to get started at school")
elif age > 7 and age < 12:
    print ("Primary school")
elif age > 12 and age < 15:
    print ("High school")
elif age > 15 and age < 17: 
    print ("Intermediate")
else:
    print ("World is a university")

"""
Comparing each item in a list to one in the other list
"""
cars_i_have = ["verna", "creta", "Lancer", "premier"]
cars_to_get = ["Rolls Royce", "Jaguar", "creta", "Mustang", "Lambo"]
purchase_order = []

# I will check each car I have against the car i want to get and will update the purchase order list

for cars in cars_to_get:
    if cars in cars_i_have:
        print (f"You are sorted out. You already have {cars}.Enjoy the drive")
    else:
        purchase_order.append(cars)
print(f"order these cars {purchase_order}")

#Checking if the list is empty 
if purchase_order: #if the list is passed to the if statement it returns True if the list is not empty
    print ("Why the wait...order it")
else:
    print ("glad you have nothing to order. Enjoy your pipe")




















# In[ ]:




