import sys

# File:    project2.py
# Author:  Victor Gee
# Date:    11/29/2014
# Section: 07
# E-mail:  vicgee1@umbc.edu
# Description:
# This file contains python code that will recursively
# traverse a maze, specified by a text file
# the text file specifies in its first row the number of rows and columns in the maze
# every line after that is four digits long corresponding to each wall of the cells

def printGreeting():
    # function welcomes the user to the program
    # Input: none
    # Output: only outputs to the screen the welcome message
    print("Welcome to the Maze Traveler.")
    print("This program will solve mazes using a recursive search.")
    return

def processCommandLineArgs():
    # accepts arguments from the command line, verifies
    # that the number of arguments are given is correct
    # Input: none
    # Output: returns None if number of arguments is incorrect
    # and assigns command line arguments to variables if 
    # number of arguments is correct then returns those variables
    if len(sys.argv) != 6:
        print("Incorrect number of arguments given.")
        return None, None, None, None, None
    else:
        return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

def openFile(fileNombre):
    # this function is responsible for accepting user input for the filename of maze specifications
    # in addition, this function parses the lines of the file into a three-dimensional array
    # which makes up the maze
    # Input: this function does not require any arguments
    # Output: this function will return the maze to the main call

    # exception handling for when a name is entered for a file not in the directory
    while True:
        try:
            #fileName = input("Enter the file name of the maze specification.")
            inFile = open(fileNombre, 'r')
            break
        except FileNotFoundError:
            print("Oopsies!  That file does not exist in this directory. Try again. ")
            fileNombre = input("Re-enter a file name. ")
    return inFile

def readMazeFile(file_name, start_rpos, start_cpos, end_rpos, end_cpos):
    # function will create the maze based on input from file
    # Input: takes a filename, and the start and end positions as integers
    # Output: returns a constructed maze
    # for loop iterates over text file to take in maze size and wall information
    maze = []
    for i, line in enumerate(file_name):
        # at the first line of the file are the rows and columns specifications
        # the first line is vigourously input checked, they must be pure
        # these two numbers are assigned to variables named rows and columns
        if i == 0:
            blankSpace = line.index(" ")
            rows = ''
            columns = ''
            
            for i in range(0,blankSpace):
                rows += line[i]
    
            for j in range(blankSpace, len(line)):
                columns += line[j]

            for i in range(len(rows)):
                if rows[i].isdigit() == False:
                    print("\nNon-digit found in row's position, please review maze specification.")
                    return None
                            
            rows = int(rows)
            columns = int(columns)

            if start_rpos.isdigit() == False or start_cpos.isdigit() == False or end_rpos.isdigit() == False or end_cpos.isdigit() == False:
                print("\nPlease verify that the numbers you entered for the starting and ending positions are all non-numeric.")
                return None
            # if the rows specified in start position is not contained in maze return None
            elif int(start_rpos) < 0 or int(start_rpos[0]) > int(rows):
                print("\nPlease check your start position's row value again, it is not in bounds.")
                return None
            elif int(start_cpos) < 0 or int(start_cpos) > int(columns):
                print("\nPlease check your start positions column value again, it is not in bounds.")
                return None

            elif int(end_rpos) < 0 or int(end_rpos) > int(rows):
                print("\nPlease check your end position's row value again, it is not in bounds.")
                return None
            elif int(end_cpos) < 0 or int(end_cpos) > int(columns):
                print("\nPlease check your end position's column value again, it is not in bounds.")

        # for the remainder of the lines, simply append them to the maze array
        elif i > 0:
            # .strip() removes the whitespace in the line
            # .split() converts items in line to an array
            # once these two operations are complete
            # the new array is assigned to an array called lineStripped
            lineStripped = (line.strip().split())
            # for loop iterates through the lineStripped array
            # casting each number to an integer
            # for use in spelling out the walls of the maze
            for j in range(len(lineStripped)):
                lineStripped[j] = int(lineStripped[j])
            # test print demonstrates that the new array is an array of
            # integers, no longer strings
            # print(lineStripped, end = '\n')
            # proofing complete and the new array is appended to the maze array
            maze.append(lineStripped)
    # for loop printing the values in the maze array,
    # integer casting and reading in lines successful
    # while loop indices through the maze array
    # inner, for loop limits the sub-arrays to a
    # limit the row size to the number equal to the
    # number of columns in the maze
    squareRow, rowCompilation = [], []
    index = 0
    mazeCopy = maze[:]
    mazeWidth = int(columns)
    mazeRows = len(mazeCopy)
    while index < mazeRows:
        for i in range(mazeWidth):
            squareRow.append(mazeCopy[index])
            index += 1
        rowCompilation.append(squareRow)
        squareRow = []
    
    return rowCompilation

def searchMaze(maze1, start_rowp, start_colp, end_rowp, end_colp):
    # function searches through the maze looking for all squares with open walls
    # Input: (1) the maze to look through (2) start and end coordinates
    # Output: returns the list of coordinates of open walled squares
    path1, openSquares, squares, counter1= [], [], [], 0
    
    for i in range(len(maze1)):
        for j in range(len(maze1[0])):
            for k in range(len(maze1[0][0])):
                coordinate = [i,j]
                if maze1[i][j][k] == 0:
                    openSquares.append(coordinate)
                    # if the coordinate is already in the list, remove the extra
                    if openSquares.count(coordinate) != 1:
                        openSquares.pop()
    print("Running maze search...")
    if [start_rowp, start_colp] not in openSquares:
        print("No possible solution.")
        exit()
#    path1.append([start_rowp, start_colp])

    searchMazeRecurse(maze1, start_rowp, start_colp, end_rowp, end_colp, 0, path1)


#    path_hitherto = [int(start_rowp), int(start_colp)]
#    searchMazeRecurse(maze1, openSquares, int(start_rowp), int(start_colp), int(end_rowp), int(end_colp), path_hitherto)

    # if the start and the end positions are both not in the openSquares list,
    # we already know that there cannot be a possible path 
    # return the coordinates of open squares as a list
    return openSquares



def searchMazeRecurse(maze, start_r, start_c, end_r, end_c, index, path = [], counter = 0):
    # function searches for a path to the goal
    # try each of four directions from this point until we find a way out.
    # Input: the maze to traverse, start & end positions, a stack of the path and a counter that 
    # increments during each recursive call
    # Output: returns the solution to be printed by printPath(solution_path)

    #################################################################################################
    ######################################### BASE CASES ############################################
    #################################################################################################

    #  1. OUT OF BOUNDS
    if start_r <= -1 or start_r >= len(maze):
        return False
    if start_c <= -1 or start_c >= len(maze[0]):
        return False    

    #  2. WALL IN THE WAY, return false
    if maze[start_r][start_c][index] == 1:
#        print("Wall at: ", start_r, start_c, index)
#        print("maze", maze)
#        print("start r and start c", start_r, start_c)
#        print("maze startr", maze[start_r])
#        print("maze startr startc", maze[start_r][start_c])
#        print("maze[startr][startc][index]", maze[start_r][start_c][index])
        if counter == 0:
            counter += 1
        elif counter != 0:
            return False
    counter += 1

    #  3. We have found an opening that has already been explored or is a dead end
    if [start_r, start_c] in path:
        return False

    #  4. From the tests above, We have found an outside edge not occupied by an obstacle
    #    such a square will be something to add to the path and or be the goal
    if (start_r == end_r and start_c == end_c):
        path.append([start_r, start_c])
        printPath(path)
        return True
    else:
        path.append([start_r, start_c])

    #################################################################################################
    ###################################### RECURSIVE PARTS ##########################################
    #################################################################################################

        discovery = searchMazeRecurse(maze, start_r, start_c - 1, end_r, end_c, 0, path, counter) or \
            searchMazeRecurse(maze, start_r, start_c + 1, end_r, end_c, 2, path, counter) or \
            searchMazeRecurse(maze, start_r - 1, start_c, end_r, end_c, 1, path, counter) or \
            searchMazeRecurse(maze, start_r + 1, start_c, end_r, end_c, 3, path, counter)
        if discovery:
            path.append([start_r, start_c])
        else:
            path.pop()
        return discovery
        
def printPath(stack2):
    # function will print out the path to the specified endpoint
    # Input: uses the path generated from the searchmazerecurse function
    # Output: prints to the screen the path to the endpoint
    print("Results: found the following solution path:")
    for i in stack2:
        print(i, end = "\n")

def main():

    openSquaresList = []
    printGreeting()
    # checks arguments to see that the correct number were given
    fileName, start_row, start_col, end_row, end_col = processCommandLineArgs()
    if fileName == None:
        print("")
        print("Please re-enter command with a correct number of arguments.")
        print("\n")
        sys.exit()
    elif fileName != None:
        # verifies the file name is valid otherwise reprompts
        file1 = openFile(fileName)
    # maze is created from file
    maze = readMazeFile(file1, start_row, start_col, end_row, end_col)
    if maze == None:
        print("\nExiting now.  Don't forget to check your maze spec file.")
        print("")
        sys.exit()
    openSquaresList = searchMaze(maze, int(start_row), int(start_col), int(end_row), int(end_col))

main()
