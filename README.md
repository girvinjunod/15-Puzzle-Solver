# 15 Puzzle Solver
# How to Run
## Dependencies
- Python 3.9.4 (Tested on this version, other versions may not work) 
- PyQT5

### Setup
- Install Python, preferably the same version as the one listed above 
- Run the command `pip install -r req.txt` to install the python libraries used.
- Run the command `python app.py` to run the application.
### Using the Program
- Input the 15 puzzle into the GUI by inputting numbers into the puzzle in the GUI or click the `Input from File(.txt)` button to input the puzzle through txt files. The format for the txt file can be found in the folder `test` on the file `format.txt`.
- Click the `Solve` button to solve the 15 puzzle. The steps to solve the puzzle will appear on the text box in the bottom part of the GUI. The animation for the steps to solve the puzzle will play on the right side on the GUI.
- Click the `Reset` button to reset the puzzle in the GUI into the default state.

# Algorithm
The algorithm used is the A* algorithm. The A* algorithm uses the number of tiles that are not in the correct position as the heuristic function. This is used as the heuristic function as it never overestimates the actual cost to get to the goal and that the number of tiles that are not in the correct position gives a rough estimate of how close the puzzle state is to the correct one.

The algorithms starts by estimating the cost for every single possible move that can be taken from the current puzzle state, it'll store all the possible combination of moves that has been estimated so far and then it'll choose the move that has the lowest estimate cost. This is repeated over and over again for every puzzle state chosen until the puzzle state chosen is the correct one. To prevent backtracking, a list of visited puzzle states is kept so that the algorithm doesn't choose the same puzzle state again. This is because backtracking is a guaranteed wasteful move as any move that can be taken from backtracking can be taken without backtracking.

The A* algorithm is chosen because the algorithm will find the optimal path to the solution, meaning that the solution would be shorter or at least the same to other algorithms like BFS and DFS algorithms. The A* algorithm is also very efficient as long as the heuristic function is consistent and admissible. It is important to note that due to the nature of the heuristic function, like if the heuristic function is not consistent, it's possible for the heuristic function to instead cause the solving time to be much longer that what it'd take on other algorithms like BFS and DFS algorithms. An example for this with the algorithm for this program is if the optimal solution of the puzzle is long, with the heuristic function being the number of tiles that are in the correct position, this makes the A* algorithm not efficient as it'll keep choosing the move that will move the nearest tile to the correct position but isn't a good move for the overall solution. Maybe a better heuristic function exists for the A* algorithm for solving the 15 puzzle, but the writer finds the current algorithm good enough to solve most 15 puzzle problems with the optimal solution efficiently.  
