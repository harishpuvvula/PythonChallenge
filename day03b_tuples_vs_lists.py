#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""I shall try to understand the concepts of Tuples. 
    I shall verify the immutability of Tuples. 
    Check how many list operations work on Tuples.
    I will experiment with interoperability between tuples and lists
"""
my_tuple = ("pizza", "burger", "chocolate", "eggs", "milk", "dry fruits", "chicken")

#copy between tuples
my_new_tuple = my_tuple

print(my_new_tuple)

#copy a tuple to a list

my_food_list = []

my_food_list = my_tuple
print(my_food_list)

#check the access/travesre of tuple
print(my_tuple[1])

#use for loop to traverse tuple
for tuplet in my_tuple:
    print(tuplet)
#check comprehension between tuples and lists

my_food_list = [ tuplet+" \t" + "love" for tuplet in my_tuple]
print (my_food_list)

#observation: comprehension can be used on tuples

#check slicing on tuples
#print last three items in a tuple 
print (f"Print the last three items in a tuple: {my_tuple[-3:]}")

#check list functions on tuple 

print (sorted(my_tuple))

#sort() function doesn't work on tuples given tuple is immutable. However, sorted() works

#check if list can be assigned to tuple 

mini_list = ["one", "two", "three", "four"]

my_tuple = mini_list
print (my_tuple)

#observation: you can assign a list to the tuple


#check the immutability of tuple





# In[ ]:




