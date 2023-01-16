~brief overview of the plan:

*This program comprises two parts, which I will be implementing in Python.

(1) start, middle, and end-node class objects whose locations coordinates and states are updated per iteration
    - START node: implements the A* STAR path-finding algorithm to procedurally search for the end node
    - MIDDLE node: records every square that has been passed, and implements the movement pattern per iteration by updating a list of currently travelled squares, iterating until the program has reached the end node
    - END node: does a check per iteration to note if the program has reached the end node, and breaks the program once the end node has been reached

(2) function to display a visual interface of the path-finding algorithm tracing a path from the start to end node in the terminal

----------

*Stuff I might eventually add, given the chance

(1) implementing different kinds of path-finding algorithms for the start-node (Diekstra, DFA, BFA)
(2) implement walls which can be added, and tweaking the MIDDLE node's update method to account for obstacles in movement


