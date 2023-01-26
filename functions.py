#(1) function to create a dictionary based on coordinate values 
#*takes in a template dictionary of only non-space values as arguments (format of eg. startnode = [10,10]) and returns the coordinate dictionary
#types of spaces == startnode, middlenode, endnode, empty spaces

def create_dict (**tank_dictionary):
    visual = {}
    for y in range (1,29):
        for x in range (1,57):
            for name, coordinate in tank_dictionary.items():
                if coordinate == [x,y]:
                    if name == "startnode":
                        space = "S"
                    elif name == "middlenode":
                        space = "@"
                    elif name == "endnode":
                        space = "E"
                else:
                    space = " "
                    #empty space
                visual[(x,y)] = space
    return visual

#(2) function to print said dictionary based on coordinate values
#*takes in the aforementioned output from create_dict() as arguments and prints out the display accordingly
def printer (visual:dict):
    for itervar in range (1,59):
        print ("X", end="")
    print ("\n", end="")
    for y in range (1,29):
        print("X", end="")
        for x in range (1,57):
            print(visual[(x,y)], end="")
        print("X", end="")
        print("\n", end="")
    for itervar in range (1,59):
        print ("X", end="")
    print ("\n", end="")


