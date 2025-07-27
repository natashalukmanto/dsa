def replace_and_remove(size: int, s: List[str]) -> int:
    # Removing the b's
    write_index, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count += 1
    
    # Replace the a's with 'd', 'd'
    current_index = write_index - 1
    write_index += a_count - 1
    final_size = write_index + 1
    
    while current_index >= 0:
        if s[current_index] == 'a':
            s[write_index - 1: write_index + 1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[current_index]
            write_index -= 1
        current_index -= 1
            
    return final_size