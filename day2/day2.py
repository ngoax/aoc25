import re

def sum_invalid(file_path: str) -> int:
    """ Find all invalid IDs and return sum """
    
    # parse file
    with open(file_path, 'r') as file:
        line = file.read()

    ranges = line.split(",")
    print(ranges)

    sum = 0

    # Regex for first task
    r = re.compile(r'^(\d+)\1$')
    
    # ^     - start of string
    # (\d+) - capture one or more digits (this will be first half)
    # \1    - match the exact same digits again (second half)
    # $     - end of string
    # This regex backtracks to find the split that makes both halves equal


    # Regex for second task
    r2 = re.compile(r'\b(\d+)\1+\b')
    
    # \b    - match word boundary
    # (\d+) - capture one or more digits in capture group to remember 
    # \1+   - match one or more instances of the previously matched digit
    # \b    - match word boundary

    for num_range in ranges:
        min_max = num_range.split("-")
        min = int(min_max[0])
        max = int(min_max[1])
        
        for i in range(min, max+1):
            # if r.match(str(i)):
            if r2.match(str(i)):
                sum += i
                print(f'invalid ID: {i}')

    return sum


if __name__ == "__main__":
    result = sum_invalid("day2/input.txt")
    print(f'The sum of invalid IDs is: {result}')
