#for all startnode, middlenode, and endnode, to add their coordinates to a dictionary at the end of each iteration to allow for the print function to print out said nodes 

class start_node:

    def __init__ (self, location = [25,14]):
        print ("Starting node is instantiated")
        self.location:list = location

#TO implement the SWARM path-finding algorithm by following instructions in line 12
    def search_algo (self):
        self.searched_squares = []
        #repeat the below sequence for every instance of the searching for next available square, this search_algo method will check whether all out of all 4 surrounding squares for each square coordinate in the searched_squares [list], any are not in the list. For those not in the list, they will be appended to the list, and a check will be run in a seperate method to determine if the end node has been reached (end node is in searched_squares list)
        if self.location not in self.searched_squares:
            self.searched_squares.append(self.location)
        for coordinate in self.searched_squares:
            left_1 = coordinate[0]-1 
            right_1 = coordinate[0]+1
            up_1 = coordinate[1]+1
            down_1 = coordinate[1]-1
        #implemented check to account for whether desired searched coordinate is even within allocated range
            if left_1 >= 1:
                if [left_1, coordinate[1]] not in self.searched_squares:
                    self.searched_squares.append([left_1, coordinate[1]])
            if right_1 <= 57:
                if [right_1, coordinate[1]] not in self.searched_squares:
                    self.searched_squares.append([right_1, coordinate[1]])
            if up_1 >= 0:
                if [coordinate[0], up_1] not in self.searched_squares:
                    self.searched_squares.append([coordinate[0], up_1])
            if down_1 <= 29:
                if [coordinate[0], down_1] not in self.searched_squares:
                    self.searched_squares.append([coordinate[0], down_1])
            print("search algorithm run")

    #this method is constantly run with a while loop, checking "while end_found_check == False:", to run the search_algo method
    def end_found_check (self, end_node_location):
        return (end_node_location in self.searched_squares)

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
#this END_CHECK is different from the starting node's END_FOUND_CHECK in that this end_check simply checks for when the shortest path has been arrived at, whereas the starting node's end_found_check checks for whether the end_coordinate has even been found by the path_finding greedy swarm algorithm
    def end_check (self, middle_node_location):
        if self.location in middle_node_location:
            print ("End reached")
            return True


