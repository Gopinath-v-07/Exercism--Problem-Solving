DIGITS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert(input_grid):
    # Validate input dimensions
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    numbers = []

    # Process one block (4 rows) at a time
    for block_start in range(0, len(input_grid), 4):
        block = input_grid[block_start:block_start + 4]
        result = ""

        # Process one digit (3 columns) at a time
        for col in range(0, len(block[0]), 3):
            pattern = "".join(row[col:col + 3] for row in block)
            result += DIGITS.get(pattern, "?")

        numbers.append(result)

    return ",".join(numbers)