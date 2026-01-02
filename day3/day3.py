def max_joltage(file_path: str) -> int:
    """ Part 1: Find sum of the maximum joltage from each bank, considering 2 digits """
    
    # parse file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sum = 0

    for line in lines:
        digits = [int(digit) for digit in line.strip()]
        print(digits)
        
        # Search strategy: 
            # 1. First digit: find highest number in list (except last)
            # 2. Second digit: find highest number succeeding the first digit of step 1

        # 1. First digit: highest number (except last)
        first = max(digits[:-1])
        first_idx = digits.index(first)
        print(f'Highest first digit: {first}, at index {first_idx}')

        # 2. Second digit: find highest succeeding number
        second = max(digits[first_idx+1:])
        second_idx = digits.index(second)
        print(f'Highest second digit: {second}, at index {second_idx}')

        # Put numbers together
        number = int(str(first) + str(second))
        print(number)

        sum += number

    return sum




def max_joltage_12(file_path: str) -> int:
    """ Part 2: Find sum of the maximum joltage from each bank, considering 12 digits """
    
    # parse file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sum = 0

    for line in lines:
        digits = [int(digit) for digit in line.strip()]
        print(digits)
        
        # Search strategy: 
            # 1. First digit: find highest number in list (except bottom 11)
            # 2. Second digit: find highest number succeeding the first digit of step 1
            # 3. ... repeat until 12th digit

        str_number = ""
        start_idx = 0
        
        for i in range(12):
            # How many digits need after current iteration
            remaining_needed = 12 - i - 1
            
            # Search window: from start_idx to position that leaves enough digits
            end_search = len(digits) - remaining_needed
            
            # Find maximum digit in the valid search window
            max_digit = max(digits[start_idx:end_search])
            
            # Find its position (first occurrence after start_idx)
            max_idx = digits.index(max_digit, start_idx)
            
            str_number += str(max_digit)
            
            # Next search starts after this digit
            start_idx = max_idx + 1

        number = int(str_number)
        print(number)
        sum += number

    return sum




if __name__ == "__main__":
    result = max_joltage_12("day3/input.txt")
    print(f'The total output joltage is: {result}')

