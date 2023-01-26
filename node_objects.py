#for all startnode, middlenode, and endnode, to add their coordinates to a dictionary at the end of each iteration to allow for the print function to print out said nodes 

class start_node:

    def __init__ (self, location = [25,14]):
        print ("Starting node is instantiated")
        self.location = location

#TO implement the A-STAR path-finding algorithm
    def search_algo (self, end_node_location):
        self.searched_squares = []
        if self.location not in self.searched_squares:
            self.searchedsqares.append(self.location)


class middle_node:

    def __init__ (self):
        print ("Middle node is instantiated")
        self.location = []

#method for the middle_node class object which constantly updates its list of past locations, and checks for the next move it should make
#to be invoked every iteration until the break condition for end_node check is reached
    def update (self, end_node_location):
        new_current_location = self.location[len(self.location)-1]
        vertical_dist = end_node_location[1] - new_current_location[1]
        horizontal_dist = end_node_location[0] - new_current_location[0]
        vertical_direction = "left"
        horizontal_direction = "right"
        if vertical_dist < 0:
            vertical_dist = abs(vertical_dist)
            vertical_direction = "down"
        if horizontal_dist < 0:
            horizontal_dist = abs(horizontal_dist)
            horizontal_direction = "left"

        if vertical_dist >= horizontal_dist:
            if horizontal_direction == "left":
                self.location.append([new_current_location[0]-1, new_current_location[1]])
            elif horizontal_direction == "right":
                self.location.append([new_current_location[0]+1, new_current_location[1]])
            #horizontal first

        elif horizontal_dist > vertical_dist:
            if vertical_direction == "up":
                self.location.append([new_current_location[0], new_current_location[1]+1])
            elif vertical_direction == "down":
                self.location.append([new_current_location[0], new_current_location[1]-1])
            #vertical first

class end_node:

    def __init__ (self, location = [30,27]):
        print ("End node is instantiated")
        self.location = location

#to be checked every iteration of the loop, self-breaking upon the condition
#break condition for while end_check == False: end_check algorithm 
    def end_check (self, middle_node_location):
        if self.location in middle_node_location:
            print ("End reached")
            return True


