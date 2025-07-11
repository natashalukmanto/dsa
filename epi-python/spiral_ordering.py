def matrix_in_spiral_order0(square_matrix):
    sequence = []
    if not square_matrix:
        return sequence
    directions = {
        "right": [0, 1],
        "down": [1, 0],
        "left": [0, -1],
        "up": [-1, 0]
    }
    
    row, col = len(square_matrix), len(square_matrix[0])
    index = [0, 0]
    current_direction = "right"
    visited = set()
    
    while len(sequence) < row * col:
        sequence.append(square_matrix[index[0]][index[1]])
        visited.add(tuple(index))
        
        
        next_index = [
            index[0] + directions[current_direction][0],
            index[1] + directions[current_direction][1]
        ]
        
        if (
            next_index[0] < 0 or next_index[0] >= row or
            next_index[1] < 0 or next_index[1] >= col or
            tuple(next_index) in visited
        ):
            if current_direction == "right":
                current_direction = "down"
            elif current_direction == "down":
                current_direction = "left"
            elif current_direction == "left":
                current_direction = "up"
            elif current_direction == "up":
                current_direction = "right"
            
            next_index = [
                index[0] + directions[current_direction][0],
                index[1] + directions[current_direction][1]
            ]
        
        index = next_index
    
    return sequence

# This is a good approach, but imo it's a bit too complicated
# Plus points for being able to flex your python library skills
# Going with this approach shows you deeply understand how to exploit python functions, specifically
# - you know how zip works
# - you took advantage of python's unpacking operator (*)
def matrix_in_spiral_order1(square_matrix):
    answer = []
    
    def construct_layer(layer_num):
        # Getting the center tile
        if (layer_num == len(square_matrix) - layer_num - 1):
            answer.append(square_matrix[layer_num][layer_num])
            return
        
        answer.extend(square_matrix[layer_num][layer_num:-1-layer_num]) # top row; going left to right
        answer.extend(list(zip(*square_matrix))[-1-layer_num][layer_num:-1-layer_num]) # right col; going top to bottom
        answer.extend(square_matrix[-1-layer_num][-1-layer_num:layer_num:-1]) # bottow row; going right to left
        answer.extend(list(zip(*square_matrix))[layer_num][-1-layer_num:layer_num:-1]) # left col; going bottom to top
        
    for layer_num in range((len(square_matrix) + 1) // 2):
        construct_layer(layer_num)
    
    return answer

# I genuinely think this one is the more readable solution, and perhaps more natural. It's similar to my first approach, but much cleaner.
def matrix_in_spiral_order(square_matrix):
    #direction = 0    1        2        3
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    answer = []
    
    for _ in range(len(square_matrix) ** 2):
        answer.append(square_matrix[x][y])
        square_matrix[x][y] = 0 # this is how you mark visited cells 
        new_x, new_y = x + shift[direction][0], y + shift[direction][1]
        
        if (new_x not in range(len(square_matrix)) or 
            new_y not in range(len(square_matrix)) or
            square_matrix[new_x][new_y] == 0): # at this point I didn't know that the entries in the square matrix won't be 0/won't have duplicates of 0. Hence why I made a visited set.
            direction = (direction + 1) % 4 # clever way to change directions, the book uses bitwise operator, direction = (direction + 1) & 3, but I find the modulo operator more commmonly used and therefore easier to understand
            # this cycles the direction from 0, 1, 2, 3 -> exactly all the indexes in shift 
            new_x, new_y = x + shift[direction][0], y + shift[direction][1]
        x, y = new_x, new_y
    
    return answer