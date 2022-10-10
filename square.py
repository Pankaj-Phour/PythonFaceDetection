# In this Function(file) we will be calculating the square of numbers entered by user 
# We can use input() method in Python to take a value from the user 
# By default the input() method always returns a string 
# But we can typecast that value according to our need if the value is in the format as we want to typecast 

# Printing a line to tell user what this function is all about 
print("Enter a value and Press Enter to see square of the number")

# getting a value form the user 
x = (input())

# Conditional expression 
if(x.isdigit() or float(x)):                    # Checking if the value entered by user is  a number or a float value 

    square = float(x)**2                        # calculating the square of number entered by the user in float value

    print("Square of ",x, " is " , square)      # Printing the square of the value entered by the user 

# This block will execute only if the above condition is not true 
else:                                           # if the value entered by user is neither int nor float then this block will be executed 
    print(x, " is not a number")                # Printing that the user entered a wrong value



# Checking for the type of value entered by the user 

if(float(x)):                               # This block will be executed only if the value entered by user is of type float

     print(x, " is a float.")               # Printing the value entered by user 

    # This condition will be executed only if the above condition is not true and the value entered by user is of type int 

elif(x.isdigit()):

    print(x, " is a number.")               # Printing the value entered by user

# This code block will be executed if none of the above conditions are true 

else:
    print(x , " is a string.")              # Printing the value entered by user

    
print("******************************************************************* Thank You *********************************************************************")
