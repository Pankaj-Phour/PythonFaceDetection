# Dictionary in Python 
# Dictionary is a collection of key value pairs in python 
# These key value pairs can be of any data type 
# we can have strings integers booleans and None in our dictionaries 
# Dictionary in python is same as objects in javascript 
# let's create a dictionary and learn by practical examples 



myDict = {
    'name':'Pankaj',
    'age':22,
    'mobile':9518455298,
    'post':'Angular developer',
    'bool':True
}                                           # myDict is a dictionary which is containing strings integers and bool
print(myDict)                               # Printing myDict dictionary

# Dictionary doesn't have indexing in it
# So we can't access values from dictionary using index values 
# So now, how are we gonna access values from a dictionary 
# Nothing to worry about, In dictionary we have keys and values 
# Left side values in dictionary are called keys and right side values are called value of the corresponding key 
# let's access a value from our dictionary 

# print(myDict['name'])                   # It will print the value 'Pankaj' from our dictionary as it is corresponding with the key 'name' (if present)



# we can also access a value from a dictionary by get() method 
# This is same as print(myDict['name']) except it will not raise an error if the key entered is not found in the dictionary 
# print(myDict.get('age'))                    # It will print the value associated with the key 'age' in the dictionary myDict
print(myDict.get('xyz'))                    # It will return None as the key 'xyz' is not present in the dictionary myDict



# Dictionary is different from list in Python 
# So please avoid trying list methods on dictioanry 
# Dictionary have its own methods which we will discuss later in this file 


# we can also have list in dictionary as a value of a key 
dict2 = {
    'name':"Pankaj",
    'age':22,
    'skills': ['C','Python','Javascript','HTML','CSS','Angular','React']
}
# print(dict2)
# Yiu can access the list inside the dictionary by its corresponding key 
# print(dict2['skills'])                          # It will print the value corresponding to the key 'skills' as in this case it is a list 
# And if we want to go further and print a specific value from the list at key 'skills'. We can do that by indexing because we can access values in a list by indexing as we studied in the list methods
# print(dict2['skills'][2])                       # It will first listen to the key skills and then see that its value is a list then it sees the index 2 so it prints the value at index 2 in that list

# Dictionary can have unique keys only. So if you try to add a key multiple times it will keep raplacing the previous key value pair and not add the key multiple times 
dict3 = {
    'name':'Pankaj',
    'friend':'Kundan',
    'friend':'Krishan kant',
    'friend':'chunnu'
}
# We have the key 'friends' multple times in our dictionary so let's try accessing the value of key friends 
# print(dict3['friend'])                          # It will print chunnu as the last value assigned to the key 'friend' is chunnu so it doesn't added friends multiple times. it keep replacing the old values 
# This proves that we can have unique keys in our dictionary 



# Dictionary inside dictionary 
dict4 = {
    'name':'Pankaj',
    'age':22,
    'post':'Angular developer',
    'friend': {
        'name':'Neeraj',
        'age':20,
        'post':'Ad operations executive'
    }
}

# print(dict4)                                # As we can see we are having a dictionary named dict4 and inside it at key 'friend' we are having another dictionary 

# So this is just to understand that we can have nested dictionaries of list and dictionaries 



# ************************************************************************** Dictionary Methods **************************************************************************

# keys() method 
# By this method we can print all the keys of a dictionary 
# let's see with the example of dict4 
# print(dict4.keys())                         # It will print all the keys of dict4 ([name,age,post,friend]) in this case.



# items() method 
# By this method we can get all the (key value) pairs of our dictionary 
# let's see witht he example of dict4 
# print(dict4.items())                        # It will print all the key value pairs of dict4 (('name', 'Pankaj'), ('age', 22), ('post', 'Angular developer'), ('friend', {'name': 'Neeraj', 'age': 20, 'post': 'Ad operations executive'})) in this case



# values() method 
# By this method we can get all the values from our dictionary 
# let's see it with the example of dict4 
# print(dict4.values())                   # it will print all the values of dict4 (['Pankaj', 22, 'Angular developer', {'name': 'Neeraj', 'age': 20, 'post': 'Ad operations executive'}]) the last value is a dictionary so the whole dictioanry will be printed because it was the value of key 'friend'






# *************************************************** Removal methods ******************************************************


# pop() method 
# We can also delete items (key value pairs) from our dictionary (if present)
# pop() method takes an argument (the value which you want to Delete)
# dict2.pop('name')                       # it will remove the item name from dict2
# print(dict2)
# dict2.pop('hello')                      # it will raise an error because key 'hello' is not present in our dict2
# dict2.pop()                               # it also will raise an error as pop() method requires an argument and here we didn't pass any 

# So as like list if you want to Delete a item from the end of dictionary you can use popitem() method
# print(dict2)
# dict2.popitem()                             # it will delete the item 'friend' as it is the last item in our dictionary
# print(dict2)


# clear() method 
# WE can clear the whole dictionary by clear() method 
# this method takes no arguments 
# dict2.clear()                           # it will clear the dict2 (delete all items) and now dict2 is an empty dictionary
# print(dict2)






# ********************************************** Addition methods to dictionary  ************************************************************


# update() method 
# we can add new items to our dictionary using update method 

dict2.update({'gender':'Male'})             # it will add a new key 'gender' to our dict2 
# print(dict2)

# if we want to add two dictionaries we can use update method 
# let'see with the example of dict2 and dict3 
dict2.update(dict3)                         # it will add dict3 in dict2 and update dict2 (if some keys are already in dict2 and also present in dict3 then it will replace the keys of dict2 with dict3 )
# print(dict2)


# We can also update a key or add  new key directly to our dictionary 
# updating a key 
# dict2['name'] = 'Jompak'                    # it will search for the kew 'name' in dict2 and then update it's value to 'Jompak'
# print(dict2)


# adding  a new key 
dict2['address'] = 'Gurgaon'                # looks for key 'address' if present then update it's value to gurgaon if not present then set a new key named 'address' with value 'gurgaon'
print(dict2)

