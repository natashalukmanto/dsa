def snake_string(s: str) -> str:
    # return s[1::4] + s[::2] + s[3::4]
    
    result = []
    
    for i in range(1, len(s), 4):
        result.append(s[i])
    for j in range(0, len(s), 2):
        result.append(s[j])
    for k in range(3, len(s), 4):
        result.append(s[k])
        
    return "".join(result)