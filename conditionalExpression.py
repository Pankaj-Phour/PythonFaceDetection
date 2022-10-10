
# In this program(file) we are gonna be using comparision operators 
# Comparision operators are used to compare two values 
# Below are the commonly used comparision operators 
# 1.) == This will check if the value on left side is equal to right side (returns true if values are equal returns false if values are not equal)
# 2.) != This will check if the value on left side is not equal to value on right side 
# 3.) > Checks if value on left side is greater than value on right side 
# 4.) < Checks if value on right side is greater than value on left side 
# 5.) >= Checks if value on left side is greater than or equal to value on right side 
# 6.) <= Checks if value on right side is greater than or equal to value on left side 

# All these operators will return a boolean value (Either true or false)
# if the condition satisfies then it returns true else it will return false 


# Conditional expressions are very important in any programming language 
# We can understand these by taking an example from our daily routine 
# Like if we decide to go out on a sunny day and stay home at a rainy day 
# Then the above statement is a conditional expression. Because we are saying that if it is sunny then we will go out else we will stay at home 
# Let's try the same with python conditional expresssion 
# In conditional expresssion only one code block is gonna be executed (if block or else block or elif block(if added)) which satisfies the given condition

from ast import operator
from tokenize import String


day = 'sunny'
if(day=='sunny'):
    print("We will go outside")
else:
    print("we will stay at home")

# The above program will print 'We will go outside' as it meets the first condition if (in which we are checking if the day is 'sunny' which is actually 'sunny'). 
# So it satisfies the first condition so it will print the if code block and jumps out of the conditional expresssion without even looking at the else block 


# we can also add elif in our conditional expressions with if and else blocks 
# Let's try it 

age = 15
if(age<5):
    print('You can drink milk')
elif(age<18):
    print("You can drink cold drink")
else:
    print('you can drink beer')

# The above program will print 'You can drink cold drink' as the age is 15. It first checks the if statement in which it will check if the age is less than 5 (age is 15 which is not less than 5 ).So it will not execute that if block and will move on to elif block
# Then it will check in elif block if the age is less than 18 (which actually is because age is 15 which is less than 18).So it will execute the elif block and then jump out of the conditional expression
# We can have as much elif statements in our conditional expression as much we want 
# but in a conditional expression we can have only one if condition and one else condition (else block is optional) 

# We can either have an if statement or an if statement with else statement or we can have multiple if statements or we can also have if-elif-else ladder 




# Now that we have tried comparision operators with conditional expressions 
# It's time that we should try some more methods and operators with conditional expressions 
# We can check more than 1 condition with conditional expressions in python 
# We will be using Logical operators for checking more than one condition 
# There are 3 main logical operators 
# 1.) and operator -----> It checks both conditions and return true if both the conditions are satisfied (true) (it returns false if any one of the conditions is false )
# 2.) or operator  -----> It checks both conditions and returns true if any one of the conditions is true (it returns false only when both the conditions are false)
# 3.) not operator ----->  It is used to convert a value to its opposite (like if a value is true and not operator is used with it then it will turn it to false and if the value is false then it will turn it to true) 
# Let's see by practical example 

marks = 56
if(marks>50 and marks<70):                              # here we are using and operator (It is checking both the values that if marks are greate than 50 and less than 70) if both the conditions are true only then the if block will be executed else it will move on to next elif statement 
    print("Marks are greate than 50 and less than 70")
elif(marks<50):                                         # Checking if marks are less than 50 
    print('marks are less than 50')
elif(marks==50):                                        # checking if marks are equal to 50
    print('Marks are equal to 50')
else:{                                                  # If none of the condition is true then this code block will be executed automatically 
    print("Marks are greater than 70")
}


# Taking same example with or operator 
marks2 = 79
if(marks2 >70 or marks2 >80):                           # Here we have value of marks 79 and we are checking 2 conditions here (1. if marks are greater than 70  2. if marks are gretaer than 80). Here first condition is true but second is false.But it will still execute if block because or operator return true if either one condition is true 
    print("You got good marks")
elif(marks2>50):                                        # Checking if the value of marks are greater than 50 
    print("Your marks are greater than 50")
else:
    print("Marks are lower than 50")                    # This code block will be executed only if none of the above conditions are true



# Taking same example with or operator 
marks3 = 87
if(not(marks3>80)):                                      # First checks if marks are greater than 80(which is true).then the not operator converts true value to false and if block code is not executed
    print("Marks are not greater than 80")
elif(not(marks3<80)):                                    # Checks if marks are less than 80 (which returns false). Then the not operator converts false to true and this code block is executed 
    print("Marks are not less than 80")
else:                                                    # It will execute only if none of the above conditions are true
    print("None of the above conditions are true")



# We also have is and in in Python 
# We can also use these operators with conditional expressions 

a = None                                                # Assigning none to variable a 
if(a is None):                                          # Checking if a is None
    print("Yes a is none")                              # Executing this statement if a is none
else:                                                   # if the above statement is not true then this statement will be executed 
    print("No A is not none")


# We can check for various conditions with is operator in conditional expressions 

if(a is String):                                        # Checkking if a is a string
    print("Value of a is in string format")
else:                                                   # if a is not a string then this code block will be executed
    print("Value of a is not in string format")

# We can check the same condition with type number type boolean or any value we want to compare it to 


# We also have in operator in python, Which we can use with conditional expressions 
# in operator is mostly used with lists sets etc. data types 
# Let's say we have a list of users names 

names = ["Pankaj","Kundan","Krishan Kant","Chunnu","Chandra Kishor"]                # Creating a list of user names 
if("Pankaj" in names):                                                              # Checking if Pankaj is present in the list names 
    print("Yes Pankaj is present in the names list")
else:                                                                               # If the above code block is not true then this else block will be executed
    print("Pankaj is not present in the names list")

# Let's check for a name that is not in the List names 

if("Neeraj" in names):                                                              # Checking if Pankaj is present in the list names
    print("Neeraj is present in the list")
else:                                                                               # If the above code block is not true then this else block will be executed
    print("Neeraj is not present in the list")


# Conditional expressions can be used with various arithmetic operators, comparision operators, logical operators, in and is operator, and many more things 
# Let's try a program that takes 3 values from user and gives the greatest value from the 3 values

# num1 = int(input("Enter number 1: "))                                   # Getting value from the user 
# num2 = int(input("Enter number 2: "))                                   # Getting value from the user 
# num3 = int(input("Enter number 3: "))                                   # Getting value from the user 

# Now we have 3 numbers num1, num2, num3 
# We can check with comparision operators which is the greatest from the 3 values 
# if(num1>num2):                                                          # checking if num1 is greater than num2 with comparision operator
    # winner1 = num1
# else:                                                                   # Code block will be executed if the above statement is not true 
    # winner1 = num2

# if(winner1 > num3):                                                         # checking if (greatest of num1 and num2) winner1 is greater than num3 with comparision operator
    # print(str(winner1) + " is the greatest number from the given values.")
# else:                                                                   # Code block will be executed if the above statement is not true 
    # print(str(num3) + " is the greatest number from the given values.")



# So as you seen we can do various calculations with the help of conditional expressions 
# The above method is good only if we have 2 or 3 values. But if we have multiple values then we have some other methods in python to do the same work(find out the greatest value) 
# let's try the above program with multiple values 

# number1 = int(input("Enter number 1: "))                                   # Getting value from the user 
# number2 = int(input("Enter number 2: "))                                   # Getting value from the user 
# number3 = int(input("Enter number 3: "))                                   # Getting value from the user 
# number4 = int(input("Enter number 4: "))                                   # Getting value from the user 
# number5 = int(input("Enter number 5: "))                                   # Getting value from the user 
# number6 = int(input("Enter number 6: "))                                   # Getting value from the user 


# Storing the user entered values in a list 
# numList = [number1,number2,number3,number4,number5,number6]
# print(numList)

# Now sorting the values given by user in ascending order 
# numList.sort()
# Now the greatest value will be at last index(5) 
# greatest = numList[5]

# Printing the greatest value 
# print(str(greatest) + " is the greatest number from the given values.")


# if we are having a list of users. And asks user to enter his name to login, if it is present in the list then it will say welcome else it will say no user found with that name 

# Getting value from the user 
userName = input("Enter your name: ")                                    # Getting value from the user 

if(userName in names):                                                   # Checking if the name entered by user is present in the list 
    print("Welcome "+ userName)
else:                                                                    # Code block will be executed if the above statement is not true
    print("Your name is not in the list")


# As of now if we search "PANKAJ" in the names it will print "Your name is not in the list" 
# We can also modify the above function to work it even the user enters name in capital letters or small letters 

lower = userName.lower()                                                 # converting the name entered by user to lowercase
print(lower)
for i in range(len(names)):
    names[i].lower()

if(lower in names):                                                   # Checking if the name entered by user is present in the list 
    print("Welcome "+ userName)
else:                                                                    # Code block will be executed if the above statement is not true
    print("Your name is not in the list")