"""
Trying files for the first time using pathlib 

"""

from pathlib import Path 

mypath1= Path("car.py")
file_content = mypath1.read_text()
lines = file_content.splitlines()
print (f"the files has {len(lines)} lines") #prints the number of lines

#I will write a function to print the first three lines of a file
#"lines" is the array 
for i in range(0,4):
    print(lines[i])
    
#I want to write to a file 

mypath1.write_text("#This is a test comment")
"""I will work on the finer aspects tomorrow:
- Existence of the files
- counting the files lines 
- Appending to the files
- Extraction from certain lines 
- 

"""




