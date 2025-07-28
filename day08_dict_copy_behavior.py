
"""Need to test shallow copy and deep copy in dictionaries
Alos need to list shallow copy in dictioanries
"""

dic1 = {"Harish": 45, "Shilpa": 40, "K": 6, "mummy":75}

dic2 = dic1

dic2["Pradeep"] = 40
print (dic1)
#The assignment of dictionaries work like lists. You chnage one dictionariy, the assigned dict also changes

#shallow copy

dic2 = dic1.copy() #use copy member function
dic2["PRB"] =74

print (dic1)
print (dic2)

