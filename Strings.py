

a = "This is a string"

# Length method 
print(len(a))
print(a)

# Find method 
find = a.find('string')                           # this method is used to find a specific value in string (it returns the index of first occurence of that word if present in the given string else it returns -1)
print(find)

# Slice method examples

# print(a[0:8])                                     # prints string a from index 0 to index 7
# print(a[0:50])                                    # prints string a from index 0 to 50(if string length is upto 50 else if string length is less than 50 then it prints upto the length of string in this case it is 16)
# print(a[0:len(a)])                                # prints string a from index 0 to end of string (len(a) method gives the length of the given string (16) which means this line is same as a[0:16])
# print(a[:8])                                      # prints string a from index 0 to index 7 (if starting point is not defined then it takes 0 as starting point)
# print(a[0:])                                      # prints string a from index 0 to end of string (if ending point is not defined then it takes last index as ending point)
# print(a[12:5])                                    # if we try to write the slice method in reverse format like from 8 to 5 or 12 to 4 then it is not valid and returns blank(nothing)

# Replace method 
replace = a.replace('string',"new String")        # this method is used to replace a specific word from the string with a new word (if present in the string)
print(replace)

# String formats
string1 = 'String with Single quotes'
string2 = "String with Double quotes"
string3 = '''String with Triple quotes'''

# The above variables are all string. We can write a string into any format from the above 3 formats.
print(string1)
print(string2)
print(string3)

# Multin line String method 
# print("This is a multiline String.
# This is not valid method")       # this is not a valid string and throw syntax error because it is not allowed in python. So if you want to do so you can do that by triple quotes string method


# We can write multi line strings with this method 
# print('''This is a multiline string 
# We can add multiple lines
# in these Strings 
#             the spaces will also reflect if you add spaces in your string ''')


# Input from user 
# name = input("Enter your name: ")
# print(name)                                # input() method always returns a string (even if user enters a number float boolean or anything)


# Escape characters
# String = '''My name is Pankaj. I am working as a web developer. Now i am learning Python'''     # if we write this it will be in one line and not look appropriate.
# print(String)


# So if we want to add spaces or new line to our string we can use escape characters for that 
# \n is used to add a new line and \t is used to add four spaces and \' is used to add ' to our string and \\ is used to add a \ to our string
# So basically what it does is it neglects the \ and works according to the character after \
String2 = '''My name is Pankaj.\nI am working as a web developer.\n\tNow i am learning Python'''
print(String2)


# Now we are writing a program with the above tried methods 
# we can take data from user and then print a multi line letter with the data entered by user 

Name = input("Enter your name :\n")
Date = input("Enter Date :\n")
letter = '''Greeting <|Name|>\nWe are happy to inform you that,\nYou have been selected in the ABC coding house.\nThanks and regards ABC codeing house.\nDate: <|Date|>'''
letter = letter.replace('<|Name|>',Name)
letter = letter.replace('<|Date|>',Date)
print(letter)