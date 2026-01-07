from collections import Counter

def get_grid(file_path: str) -> dict:
    """ Get grid containing coordinates and value """
    
    # Parse file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = {}

    for row_idx, line in enumerate(lines):
        for col_idx, char in enumerate(line.strip()):
            grid[(col_idx, row_idx)] = char

    # for key, value in grid.items():
    #    print(f"{key}: {value}")

    return grid


def count_adjacent_cells(grid: dict, x_coord: int, y_coord: int) -> int:
    """ Check adjacent cells and return count of occupied adjacent positions """
    # Adapted from source - https://stackoverflow.com/a/2373689
    # Posted by Justin Peel
    # Retrieved 2026-01-05, License - CC BY-SA 2.5
    result = {}
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if (x,y) in grid:
            result[(x,y)] = grid[(x,y)]
    # print(result)

    count = Counter(result.values())
    # print(f"Occupied cells: {count["@"]}")
    return count.get("@", 0)


def part1(input: str) -> int:
    grid = get_grid(input)
    free_pos = 0
    for (x, y), value in grid.items():
        if value != '@':
            continue
        count = count_adjacent_cells(grid, x, y)
        if count < 4:
            free_pos += 1
    return free_pos

def part2(input: str) -> int:
    grid = get_grid(input)
    total_removed = 0
    while True:
        removed = 0
        for (x, y), value in grid.items():
            if value != '@':
                continue
            count = count_adjacent_cells(grid, x, y)
            if count < 4:
                grid[(x,y)] = '.'
                removed += 1
                total_removed += 1
        print(f"Removed {removed} rolls in iteration")
        if removed == 0:
            break
    return total_removed


if __name__ == "__main__":
    path = "day4/input.txt"
    print(f"Part 1 - Free positions: {part1(path)}")
    print(f"Part 2 - Possible rolls to remove: {part2(path)}")