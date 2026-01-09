from functools import reduce
import operator

OPS = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.truediv
}

def parse_input_part1(file_path: str) -> int:
    """Part 1: Parse text file and return results horizontally"""
    with open(file_path) as f:
        rows = [line.split() for line in f]

    # Transpose rows → columns
    # Trick: Transpose rows → columns
    # 1. *rows - unpacks rows into separate args for zip()
    # 2. zip() - pairs up elements at the same index from each argument
    # columns = list(zip(*rows))
    columns = list(zip(*rows))
    
    result = 0
    for col in columns:
        op_func = OPS[col[-1]]
        result += reduce(op_func, map(int, col[:-1]))
    
    return result

def parse_input_part2(file_path: str) -> int:
    """Part 2: Parse text file and return results vertically"""
    with open(file_path) as f:
        lines = [line.rstrip('\n') for line in f]

    # Prepare Grid
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    char_columns = list(zip(*padded_lines))

    # Group into Blocks
    problem_blocks = []
    current_block = []
    
    for col_tuple in char_columns:
        # A column separates problems only if completely empty
        if all(c == ' ' for c in col_tuple):
            if current_block:
                problem_blocks.append(current_block)
                current_block = []
        else:
            current_block.append(col_tuple)
    
    if current_block:
        problem_blocks.append(current_block)

    # Process Blocks
    total_result = 0

    for block in reversed(problem_blocks):
        numbers = []
        op_func = None
        
        for col in reversed(block):
            char_at_bottom = col[-1]
            num_str = "".join(col[:-1]).strip()
            
            # Check for operator
            if char_at_bottom in OPS:
                op_func = OPS[char_at_bottom]
            
            if num_str:
                numbers.append(int(num_str))

        if numbers and op_func:
            total_result += reduce(op_func, numbers)
            
    return total_result

if __name__ == "__main__":
    path = "day6/input.txt"
    print("Part 1:", parse_input_part1(path))
    print("Part 2:", parse_input_part2(path))