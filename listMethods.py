# List is a collection of values in Python 
# They are known as Array in javascript 
# They have length property, We can access its elements(values) from index no.
# Indexing of a list starts from 0 
# List can contain values of any data type 
# Lets start and have a look at list structure and methods in python 



list = ["Pankaj",2,"Kundan",4,"Krishan Kant",1,"Chandra",8]     # As we discussed earlier a list can have values of any data type
print(list)                                                     # Print the list values



# Some of the most used List methods
# len() method ( It gives as the number of total values in the list)
print(len(list))                            # len() method  is used to get the length of a list

# Accessing values from a list by index no.
# print(list[0])                  # This will give us the first element in the list
# print(list[4])                  # This will give us the 5th element from the list




# ******************************************************************* Slicing methods *******************************************************************
# slicing of list 
# By this method we can use index values of list and slice it from wherever to wherever we want 
# First value in the slice method is included while the second value is excluded
# Which means that in the line below list will start printing values from index 0 and goes upto index 2 and not print value on index 3 
# print(list[0:3])                # This will print the items from mindex 0 to index 2 
# print(list[3:7])                # This will print the items from mindex 3 to index 6 

# We can also pass only ending point by slice method and it will take 0 by default as starting point 
# print(list[:4])                 # Here we passed only ending point (4) So it will automatically start from 0 and prints upto index 3

# Similarly we can also pass only starting point and it will take end of list as ending point by default 
# print(list[4:])                 # This will start printing from index 4 and goes upto end of list 

# We can also have both starting and ending point blank and it will still work and take 0 as starting point and end of list as ending point 
# print(list[:])                  # But this doesn't make any sense beacuse if we want ton print the whole list. We can just simply write print(list)

# We can also use slicing to print some values and leave others from list in format 
# Basically what i want to do is pass a third parameter to slice method and tell python intrepretor to print the specific values only 
# print(list[0:8:3])               # This line of code is starting printing from index 0 of list and goes upto index 8 in list(if present else end of list) and prints every 3rd value escaping 2 values between 
# So the third parameter tells python interpretor which value is gonna be printed and how many values it have to escape(ignore) 
# print(list[0::2])                # So this line is starting from 0 and second parameter is blank so it will go upto end of list and third parameter is 2 so it will print every second value from the list escaping one value between





# ******************************************************************* Addition methods *******************************************************************
# Append method 
# By append method we can add values to our list 
# Append method adds values at the end of the list
# list.append("Chunnu")           # 'Chunnu' will be added in the list at last index(end of list)
# print(list)
# list.append(2,"Ajay")           # it will raise an error because append method only takes one parameter (it can add only one value at a time)
# print(list)

# Insert Method 
# By insert method we can add values to a specific index
# It takes two parameters (first is index no. where to insert the value and second is the value itself) 
# We can insert a value at any index(place) in the list by Insert() method 
# list.insert(3,"newValue")       # It will insert "newValue" at index 3 in the list
# print(list)
# list.insert(3,1,2,3,4,5)            # This will raise an error as insert() method takes only two parameters (first is index no. where to insert the value and second is the value itself)
# list.insert(3,[1,2,3,4,5])          # If we want to add multiple items by insert method then we can pass them in a list and then add the list at that index in list
# print(list)

# Extend method 
# If we want to add multiple items in a list then we can use extend() method 
# We pass a list as parameter in the extend() method
# list.extend([1,2,3,4,5,7])       # items 1,2,3,4,5,6,7 will be added at the end of list
# print(list)

# We can also create another list and then add it to our list by extend() method 
newList = ["Item1","Item2","Item3"]
# list.extend(newList)               # newList items will be inserted at the end of our list
# print(list)




# ******************************************************************* Removal methods *******************************************************************
#  if we want to remove items from our list then we can use these methods

# remove() method 
# This method is used to remove a specific value from the list (if present)
# remove() method takes one parameter (the value itself to delete from the list) 
# list.remove("Pankaj")               # This will remove Pankaj from the list
# list.remove("Neeraj")               # This will raise an error as "Neeraj" is not present in the list
# print(list)


# pop() method 
# This method is used to remove a value at specific index in the list (if present )
# pop() method takes one argument as index no. (which index no. item to delete) 
# list.pop(0)                     # This will remove item at index 0 from the list 
# list.pop(17)                    # It will raise an error as index 17 is not in the list 
# list.pop(0,1,2)                 # This will also raise an error as pop() method only takes one parameter (we can delete one by one with pop() method)
# print(list)



# clear() method 
# This method is used to clear the whole list 
# It takes no parameter(arguments) 
# list.clear()                    # It will clear the whole list and our list is empty now 
# print(list)



# ******************************************************************* Find method *******************************************************************
# if we want to find the index of any value in the list then we can use index() method 
# index() method 
# This method takes a value (as argument) to search for in the list and will return the index of the value in the list (if present )
index = list.index("Pankaj")            # It will return 0 the index no. of "Pankaj" from the list
# print(index)
# What if we pass  a value that is not present in the list 
# index2 = list.index("Neeraj")           # It will raise an error as "Neeraj" is not present in the list
# print(index2)


# index() method with additional parameters (start and end point)
# These start and end point will tell the pytohn interpretor the points where to start the search for index no. of given value and upto which it has to search 
# These are optional points 
# Suppose we want to search for a value from index 3 to index 6
# Then we can pass 3 and 6 as start and end point to index() method 
# The start and end parameters are as same as slice method. if we don,t pass the start point it will automatically take 0 as starting point and if we don't pass ending point it will automatically take end of list as ending point 
index3 = list.index(4,3,6)              # It will search for value 4 in the substring from index 3 to index 6 in the list
# print(index3)




# ******************************************************************* Count Method *******************************************************************
# if we want to count the occurence of a value in the list then we can do it by count() method 
# it takes one argument (the value) to search count for in the list 
# lets say if we add another list with numbers (1,2,3,1,2,3) to our list 
numList = [1,2,3,1,2,3]                 # Creating a list with numbers
# list.extend(numList)                    # Adding numList to our list by extend() method
# print(list)
# Now searching for occurence of a value in the list 
count = list.count(1)                   # It will look for the occurence of 1 in the list and return the no. of occurence of 1 in the list 
# print(count)
count2 = list.count(123)                # It will look for 123 in the list as 123 is not present in the list so it will return 0 and not an error 
# print(count2)





# ******************************************************************* Sort Method *******************************************************************
# For sort method we must have list of one data type (either of strings or of numbers ) not mixed up with various data types 
# so create a list of numbers first 
numbers = [1,2,34,23,345,432,232.112,1234,435]
# print(numbers)                      # Print the numbers list as it is written
numbers.sort()                      # Sorting the numners list by sort() method (in ascending order)
# print(numbers)                      # Printing the sorted list

# if we want to print the list in descending order. Then we can pass an extra argument to sort() method 
# numbers.sort(reverse=True)          # if we are passing argument reverse = True then it will first sort the list in ascending order and then reverse it to descending order
# print(numbers)

# Now lets create a list of strings and try sort() method on it 
names = ["Pankaj","Krishan Kant","Kundan","Chunnu","Chandra","Ajay","Surender"]             # Creating a list with string values
# print(names)                                                                                # Printing the names list
# names.sort()                                                                                # Sorting the names list (By default it will sort alphabatically)
# print(names)                                                                                # Printing the sorted list 
# names.sort(reverse=True)                                                                    # Sorting the names list with extra argument (reverse=True) which will reverse the list 
# print(names)                                                                                # Printing the sorted list 

# We also have an other argument named Key which will tell python intrepretor on what basis it have to sort the list 
# let's create a function which returns the length of strings 
def length(e):
    return len(e)

# now lets sort the name list on basis of length of names 
# names.sort(key=length)                                                                      # our list will now be sorted according  to the length of the names strings 
# print(names)                                                                                # Printing the sorted list 

# Now passing both arguments Key and reverse in sort() method 
# names.sort(key=length,reverse=True)                                                         # It will now sort() the list according to length of strings and then reverse it 
# print(names)                                                                                # Printing the sorted list




# ******************************************************************* Reverse Method *******************************************************************
# It just reverse our list from left to right 
# Like the values from end will be at Starting now and the values at start will be at end now 
# Let's see by an example 
randomList = [1,"Pankaj",2,"Kundan",3,"Krishan Kant",4,"chunnu",5,"Surender",6,"Chandra",7,"Ajay"]
# print(randomList)                                                                           # Printing the randomList
# randomList.reverse()                                                                        # It will reverse our randomList
# print(randomList)                                                                           # Printing the reversed randomList




# ******************************************************************* Copy Method *******************************************************************
# We can also make copy of our list 
# copy() method 
copyList = randomList.copy()                                                                  # Copies our randomList to copyList
# print(copyList)                                                                               # Printing the copied copyList




# ************************************************************************** These were some of the most used functions of list *****************************************************************************