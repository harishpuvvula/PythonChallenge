"""Excercise from Python Crash Course by Eric Matthes.
Excercise 4.1. Pizzas
- Attempted range() function.
- use list stastical functions min, max, sum"""

my_pizza = ["Pepperoni", "Hawaiaan", "Neapolitan"]
for pizza in my_pizza:
    print ("I like \t" +pizza)
##Range function for populating numerical lists
my_range = []
i= 0
for value in range(1,5):
   my_range.append(value ** 2)
print (my_range)   

#other way to use range() to populate lists
my_list = list(range(5))
print(my_list)

#Use range functions with skip or increment 
my_oddlist = list(range(1,12,2))
print (my_oddlist)

#square the numbers 
my_square = [ ]
for value in range (1,11):
    my_square.append(value **2)
print (my_square)

#create a squared numbers for the first 10 integers using list comprehension
my_square_list = [value**2 for value in range (1,11)]
print (my_square_list)
################################
print (max(my_square_list))
print (min (my_square_list))
#find the sum of first N numbers. Accept the user input. Evaluate if the input is number
my_num = int(input(print("Enter the Number"))) #convert the number to integer
if isinstance(my_num, int):
    my_list = list(range(1, my_num+1))
    print(sum(my_list))
#Excercise 4.3: Use for loop to print the number from 1 to 20
twenty= list(range(1,21))
print (twenty)
# sum of the first million numbers
twenty= list(range(1,1000000))
print (sum(twenty))

#Excercise 4.7 make the list with multiples of 3s from 3 to 30. 
three_times = [i*3 for i in range(1,11)]
print (three_times)

#Excercise 4.8 and 4.9: print the first 10 cubes
my_cubes = [i**3 for i in range(1,11)]
print (my_cubes)

