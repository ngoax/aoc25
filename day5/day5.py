def parse_input(file_path: str) -> tuple[list, list]:
    """ Parse text file and return ranges and IDs """
    with open(file_path, 'r') as file:
        ranges_ids = file.read().strip().split("\n\n")
        
    ranges = []
    for r in ranges_ids[0].splitlines():
        low, high = r.split("-")
        ranges.append((int(low), int(high)))

    ids = list(map(int, ranges_ids[1].splitlines()))
    
    return ranges, ids


def part1(ranges: list, ids: list) -> int:
    """ Check if IDs are in valid ranges """
    count = 0
    for id in ids:
        for low, high in ranges:
            if low <= id <= high:
                count += 1
                break
    return count

def part2(ranges: list) -> int:
    """ Merge overlapping ranges and count total IDs """
    # Source: https://dev.to/grantdotdev/using-python-to-merge-array-of-ranges-2hic, Grant Riordan
    sorted_ranges = sorted(ranges)

    # Merge overlapping ranges
    merged = []
    for start, end in sorted_ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - merge with last range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # No overlap - add new range
            merged.append((start, end))

    # Calculate total count from merged ranges
    total_count = sum(end - start + 1 for start, end in merged)
    return total_count



if __name__ == "__main__":
    path = "day5/input.txt"
    ranges, ids = parse_input(path)
    
    print(f"Part 1 - Fresh ingredient IDs: {part1(ranges, ids)}")
    print(f"Part 2 - Total IDs in ranges: {part2(ranges)}")