import re

def rotate_dial(file_path: str) -> int:
    """ Calculate final password by rotating dial and counting occurences of 0 (part 1) and bypasses of 0 during rotation (part 2)"""
    
    # parse file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start = 50 # predifined starting position
    current_pos = start
    rotation_0 = 0 # times dial is pointing at 0 during or at end of rotation

    r = re.compile("([A-Z]+)([0-9]+)") # regex logic for splitting alphabetic chars and numbers 

    for line in lines:
        match = r.match(line)
        if match:
            items = match.groups()
            direction = items[0] # 'L' or 'R'
            shift = int(items[1]) # number of shifts
            if direction == 'L':
                new_pos = current_pos - shift
                if current_pos == 0:
                    # If starting at 0, count only full wraps, excluding landing
                    rotation_0 += (shift - 1) // 100
                elif shift >= current_pos:
                    # Count passing 0, excluding the landing if we land exactly on it
                    rotation_0 += 1 + (shift - current_pos - 1) // 100
                current_pos = new_pos % 100
            if direction == 'R':
                new_pos = current_pos + shift
                # Count passing 0, excluding the landing if we land exactly on it
                rotation_0 += (shift + current_pos - 1) // 100
                current_pos = new_pos % 100
            if current_pos == 0:
                rotation_0 += 1
            
    return rotation_0



if __name__ == "__main__":
    result = rotate_dial("day1/input.txt")
    print(f'The password is: {result}')
