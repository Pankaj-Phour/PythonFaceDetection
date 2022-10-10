import math


def Pankaj(a):
    if(a>1):
        result = a * Pankaj(a-1)
        print(result)
    else:
        result = 1
    return result

print("Simple function")
Pankaj(10)

x = 10
for i in range(x):
    print(i)
    print(math.sqrt(i))
    print(i**2)


