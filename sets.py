# Sets in Python are mostly similar to list in python 
# Except set can only have unique values only 
# we can access values from set by index no. as we have done in list 
# we can not manipulate (change) values of a set 
# let's see more about sets with examples 
# A set is unordered collection of values 
# These values can be of any data type 
# Set can't have list or dictionary as its items because they are ediatable(can be changed) and we can't change a set 




mySet = {11,21,3,1,4,5,6,7,8,12,9}
print(type(mySet))

print(mySet)
print(len(mySet))


# *************************************************************** Set Methods *************************************************************** 
# removing items from set 
# remove() method
# remove() method removes a specific value from the set (if present) 
# remove() method takes one argument (the value you want to delete) 
# mySet.remove(11)                          # This will remove 11 from the set 
# mySet.remove(1)                           # This will raise an error as 1 is not present in the set 
# print(mySet)



# pop() method 
# This method is also used to Delete items from a set 
# This method takes no arguments and delete a value from the set  
# mySet.pop()                               # It will delete an item from the set
# print(mySet)


# clear() method 
# This method is used to clear the whole set 
# This method takes no arguments 
# mySet.clear()                       # It will clear the whole set and return the blank set 
# print(mySet)



# ********************************************** Addition of items in sets ******************************************************
# add() method 
# This method is used to add items in set 
# This takes one argument (the value you want to add in the set) 
mySet.add('Pankaj')                       # It will add 'Pankaj' to the set           
print(mySet)




# Empty set declaration method 
# If we want to declare an empty set 
# Then most of the guys will think that we just assign {} this to a variable and it will be an empty set 
# But it's not, Let's see
# set1 = {}                           # It will be decalred as an empty dictionary 
# print(type(set1))                   # It will give output as <class 'dict'>

# So if you want to create an empty set Then this is the right method to do that 
# set2 = set()                        # It will create an empty set 
# print(type(set2))                   # It will return <class 'set'>
# print(set2)

