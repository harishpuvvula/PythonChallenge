""""Practice list Operations.
Tried insert, deletion, remove, append, pop, sort, sorted
"""
family = ["Harish", "Shilpa", 39, "Kiaan", 6]
family.append("Jyothi")
family.append("Pradeep")
#insert a value in the penultimate position
family.insert(-1, 66)
family.insert(0, "Ranga Babu")
family.insert(1, 72)
#insert value as the last item instead of using append()
family.insert(len(family), "Aruna")
family.append("Aruna")
#delete the last item in the list
del family[-1] 
#I can use pop() to delete the item and capture the deleted item to a variable

my_popped = family.pop()
#print(family)
#print (my_popped)

#To convert all the items to an upper case. There are int obejcts here and hence it will throw an error
#I shall use a for loop and handle them

"""The below for loop prints the list item type is a String"""
for members in family:
    if type(members) == str:
        print(members)
#---------------------------------------------------#
"""I can also do that using isinstance() also"""
for members in family:
    if isinstance(members, str):
        print (members)

"""I want to convert all the string items to Uppercase permanently"""
for i in range (len(family)):
    if isinstance(family[i], str):
        family[i]= family[i].upper()
print (family)

"""Deleting item by the value:
   del listname[index] removes the item by position
   remove: list.remove(value) removes the first occurence 
   this is a case senitive operation
"""
family.remove("PRADEEP")
print (family)

#### Sorting Lists##############
"""use listname.sort() to permanently sort the items. When no parameter is passed, the list is sorted in the ascending order.
   use listename.sort(reverse=True)
   To sort items temporarily use the sorted function sorted(list_name)
   Both the sort() and sorted() function do not work on the list that is the combination of int and strings
"""
#To convert only the list items to strings
#use list comprehension
sorted_family = [members for members in family if isinstance(members,str)]
sorted_family.sort()
print(sorted_family)