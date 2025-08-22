from typing import List

def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(str_part: str):
        return len(str_part) == 1 or (str_part[0] != '0' and int(str_part) <= 255)
    
    result, part = [], [''] * 4
    for i in range(1, min(4, len(s))):
        part[0] = s[:i]
        if is_valid_part(part[0]):
            for j in range(1, min(4, len(s) - i)):
                part[1] = s[i:i + j]
                if is_valid_part(part[1]):
                    for k in range(1, min(4, len(s) - i - j)):
                        part[2], part[3] = s[j + i: i + j + k], s[i + j + k:]
                        if is_valid_part(part[2]) and is_valid_part(part[3]):
                            result.append('.'.join(part))
                            
    return result