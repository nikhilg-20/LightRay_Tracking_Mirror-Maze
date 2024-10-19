def maze_solver(maze):
    # Maze dimensions
    rows = len(maze)
    cols = len(maze[0])
    
    #  Directions: right, down, left, up 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0  #  moving right
    
    # Start from this point
    position = (0, 0)
    path = [position]
    
    while True:
        r, c = position
        
        # Moving in the current direction
        dr, dc = directions[direction]
        next_r, next_c = r + dr, c + dc
        
        # Checking if light taken the exit
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break
        
        # Updating the position
        position = (next_r, next_c)
        path.append(position)
        
        # Checking the current cell to check what is in it
        current_cell = maze[next_r][next_c]
        
        # Adjusting the direction
        if current_cell == 1:  #  45-degree mirror
            if direction == 0:  #  moving Right →  to up
                direction = 3
            elif direction == 1:  #  moving Down → to Left
                direction = 2
            elif direction == 2:  #  moving Left → to down
                direction = 1
            elif direction == 3:  #  moving Up → to Right
                direction = 0
        elif current_cell == -1:  #  -45-degree mirror
            if direction == 0:  #  moving Right → to down
                direction = 1
            elif direction == 1:  #  moving Down → to Right
                direction = 0
            elif direction == 2:  #  moving Left → to up
                direction = 3
            elif direction == 3:  #  moving Up → to Left
                direction = 2
    return path

# given example
maze = [
    [0, 0, 0, -1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [-1, 0, 0, 0]
]
# Testing the function given
path = maze_solver(maze)
print(path)
