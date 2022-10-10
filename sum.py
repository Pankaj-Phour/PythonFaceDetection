
# We can use input() method in Python to take a value from the user 
# By default the input() method always returns a string 
# But we can typecast that value according to our need if the value is in the format as we want to typecast 
# In this function(file) we will be using print() method input() method and typeCasting from string to int 
# And we will also be using conditional expressions with arithmetic operators 

# Printing a line 
print("Enter two values and press Enter key to see the sum of the values")

# Taking two values from the user and assigning them to variable x and y 

x = input()
y = input()

# x and y for now is a string even if the user entered a no. (because input() method returns string only) 

# In this condition we are checking if the first value entered by user is a not a number and not a float 
if(not x.isdigit() or not float(x)):
    # This block will be executed only if the above condition is true 
    print(x," is not a number")             
    print("Please enter numeric values only")

# In this condition we are checking if the second value entered by user is a not a number and not a float
elif(not y.isdigit() or not float(y)):
    # This block will be executed only if the above condition is true
    print(y," is not a number")
    print("Please enter numeric values only")

# In this condition we are checking if the values entered by user are either of type int or of type float
elif((x.isdigit() or float(x)) and (y.isdigit() or float(y))):
     # This block will be executed only if the above condition is true
    x = int(x)              # Converting x from string to int
    y = int(y)              # Converting y from string to int
    z = x+y                 # Adding both x and y and assigning the sum to a variable named z 

    print(z)                # Printing the sum of both x and y

    print("sum of ",x, " and ", y ," is = ", int(x+y))          # confirming that the sum of x and y will be of int type

else:
    # This block will be executed only if none of the above conditions are true
    print("Function can't be executed")



print("******************************************************************* Thank You *********************************************************************")