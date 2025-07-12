from typing import List

def rotate_matrix0(square_matrix: List[List[int]]) -> None:
    if not square_matrix: return []
    
    square_matrix_copy = copy.deepcopy(square_matrix)
    
    for i in range(len(square_matrix)):
        for j in range(len(square_matrix)):
            square_matrix[j][i] = square_matrix_copy[i][j]
            
def rotate_matrix(square_matrix: List[List[int]]) -> None:
    # 4-way swap. For each layer in the square_matrix, you swap n-1 times. 
    for i in range(len(square_matrix) // 2): #i is the layers. Notice how we didn't do len(square_matrix) + 1 like problem 5.18 because the center tile won't swap with anything. Their place is still there.
        # In a 4x4 2D matrix, i will go 0, 1, 2, 3
        for j in range(i, len(square_matrix) - 1 - i): # It was natural for me to write for j in range(len(square_matrix) - 1), but here I forgot that I also wanted to take note of which layer I'm on (hence explains starting with i variable). And why len(square_matrix) - 1 - i? len(square_matrix) - 1 is trivial, we would simply overswap to many things if we didn't have the -1, but -i is to stop swapping the outer layers as well.
            # In a 4x4 2D matrix, j will go 0, 1, 2
            # 4-way swap happens here
            # 1                     4                       16                      13
            square_matrix[i][j], square_matrix[j][-1-i], square_matrix[-1-i][-1-j], square_matrix[-1-j][i] = square_matrix[-1-j][i], square_matrix[i][j], square_matrix[j][-1-i], square_matrix[-1-i][-1-j]
            # I got super confused as to why we had to swap the places of i and js, if you are too. Consider looking up reflection vs. rotation
            # Reflection: Definition: Flips a shape over a line of reflection (like the x-axis or y-axis). Examples: (x,y)→(−x,y): reflection over the y-axis and (x,y)→(x,−y): reflection over the x-axis. Orientation flips (like in a mirror)
            # Rotation: Definition: Turns a shape around a fixed point (center of rotation) by a certain angle. Examples: (x,y)→(−y,x) is a 90° counterclockwise rotation about the origin. Orientation changes (clockwise vs counterclockwise)
