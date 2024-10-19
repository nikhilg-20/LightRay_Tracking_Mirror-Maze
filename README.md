# Mirror-Maze

In this project, I will implement a function to track the path of light ray inside a mirror maze.

The mirror maze will be inputted as a 2D list argument. 

For example:
maze = [[ 0, 0, 0, -1],
        [ 1, 0, 0, 1],
        [ 0, 0, 0, 0],
        [-1, 0, 0, 0]]
represents a mirror maze in 4x4 space. 

The space is virtually divided into 16 cells. Each cell contains a number, which represents the configuration in that cell:

<img width="208" alt="Screenshot 2024-10-19 at 12 55 00 AM" src="https://github.com/user-attachments/assets/c7d13085-9ac7-40b6-bab9-982acbf96ad0">

The above 2D list maze example can be visualized as the following maze:

<img width="294" alt="Screenshot 2024-10-19 at 12 56 01 AM" src="https://github.com/user-attachments/assets/63741eb5-a5de-461e-8f02-ff827e30eeef">

Assuming the light ray always comes from the left side horizontally entering the top-left square. 

In thi specific example, the light ray will hit those four mirrors and change its direction in this maze, until it goes out of the maze.

Our function maze_solver should take that 2D list as the input maze and output the path of the light
ray travels in this maze.

For this example, the travel path is:
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
where each tuple represents the cell’s row and column index.

Your function should be called like this sample run:
Path = maze_solver(maze)
