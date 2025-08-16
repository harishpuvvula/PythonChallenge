""" 
Practise basic file operations one more time

"""
from pathlib import Path

my_path = Path("Pizza.py") #procure the path #this is something i can try for execption handling 

print(f"the file handle is of the {type(my_path)}")
print ("###########################")
#print (my_path)
my_content = my_path.read_text() #fetch text from the files

my_lines = my_content.splitlines()
for line in my_lines:
    print (line)
    
"""I checked the type of the file handler. it is of the type "Class" 
I will check the type sensitivity of the files being opened. File names are not case senitive 


"""
"""
Lets try appending a content to the file

"""

"""I shall now try to open files in the append mode
I am going to use a new approach
"""

with open("makepizza.py", "a") as f:
    f.write("#This is just comment written from another file")
    
    
""" 
"r" → read (default)

"w" → write (overwrites the file)

"a" → append (adds to the end of the file)

"r+" → read & write

"a+" → append & read
"""

""" 
prompt the user to enter a name 
append it to guestboo.txt 
print the entire file

"""

name = " "

while name != "*":
    name = input ("Ennter the guest name")
    with open("guestbook.txt", "a+") as f:
        f.write(name)
        f.write("\n")
       

my_newpath = Path("guestbook.txt")
contents = my_newpath.read_text()
print(contents)

