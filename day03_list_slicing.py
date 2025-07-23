#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Slicing function in lists
slice allows me to work with a specific group of items in a list"""

my_food = ["pizza", "burger", "chocolate", "eggs", "milk", "dry fruits", "chicken"]
my_healthy_food = my_food[3:len(my_food)]
print (my_healthy_food)

#missing the first parameter in slice. The items are sliced from the first 
print (my_food[:4])

#missing the second parameter of the slice
print (my_food[1:])

print(my_food)

#Using slice to copy list items

my_new_food = my_food[:]

print (my_new_food)
# how is that different from direct assignment 
my_new_food = my_food 
my_food.append("turkish ham")

print(my_new_food)

#a direct assignment makes sure both the lists refer to the same memory location. IT is like one location having two aliases. Hence you update on list, it automatically affects the others

my_new_food.append("pasta")

print(my_food)

#4.10: Print the first three items in the list using slice 
print(f"my first three food items are {my_food[:3]}")

# print the three items from the middle of the list to the last 
print (f"I am printing items from the middle to the last: {my_food[int(len(my_food)/2):]}")

# print the last three items in the list

print (f"I am printing the last three items in the list: {my_food[-3:]}") 

#the above is a pro tip

#print the first three items in the list
print (f"I am printing the first three items: {my_food[:3]}")

#print all the items using for loop

for fooditems in my_food:
    print (fooditems)

#want to insert a new item in the second position

my_food[1] = "Biryani"

print (my_food)

#delete an item 

del my_food[1]

print (my_food)

#remove an item by the value

my_food.remove("dry fruits")
print (my_food)

my_new_food.sort()

print (my_new_food, "\n",my_food)

my_new_food.sort(reverse = True)

print (my_food)








# In[33]:


#missing the first parameter in slice


# In[ ]:




