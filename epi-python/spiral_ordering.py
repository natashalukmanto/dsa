def matrix_in_spiral_order(square_matrix):
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

def matrix_in_spiral_order(square_matrix):
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