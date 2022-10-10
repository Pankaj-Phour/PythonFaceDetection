# In Python we can also open, close, create, delete, and modify a file according to our need with the code 
# We can add content to a file or remove content of a file or replace content of a file according to our need 

# Let's see by practical example 

# Let's first try to open a file from our folder 

f = open('sample.txt')   # Opening a file named Sample.txt 
print(f.read())          # reading the content of the file
f.close()                # Closing the file that we opened

# If we are opening a file then it is our responsibility to close the file 
