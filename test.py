
def counter(vehicles, wheels):
    if(vehicles<1 or wheels<2):
        print("Please enter valid data")
    elif(wheels<(vehicles*2)):
        print("Please enter valid data")

    else:
        fourwheelers = int((wheels - (vehicles*2))/2)
        twowheelers = int(vehicles - fourwheelers)
        print(f"Total number of four Wheelers is", fourwheelers)
        print(f"Total number of two Wheelers is", twowheelers)


counter(30,76)