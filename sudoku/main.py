def allowed(grid, row, col, digit):
    box_row, box_col = (row // 3) * 3, (col // 3) * 3
    return (digit not in grid[row]
            and all(grid[r][col] != digit for r in range(9))
            and all(grid[r][c] != digit
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)))


def solve(grid):
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        raise ValueError("Enter exactly nine rows of nine integers.")
    if any(type(digit) is not int or not 0 <= digit <= 9 for row in grid for digit in row):
        raise ValueError("Use integers 0–9; 0 means blank.")
    grid = [row[:] for row in grid]
    for row in range(9):
        for col in range(9):
            digit = grid[row][col]
            if digit:
                grid[row][col] = 0
                if not allowed(grid, row, col, digit):
                    raise ValueError("Duplicate clue in a row, column, or 3x3 box.")
                grid[row][col] = digit

    def search():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for digit in range(1, 10):
                        if allowed(grid, row, col, digit):
                            grid[row][col] = digit
                            if search():
                                return True
                            grid[row][col] = 0
                    return False
        return True

    return grid if search() else None


def main():
    print("Enter nine rows of nine space-separated digits (0 for blanks):")
    try:
        grid = [list(map(int, input(f"Row {row + 1}: ").split())) for row in range(9)]
        answer = solve(grid)
    except (ValueError, EOFError) as error:
        print(f"Invalid input: {error}")
        return
    if answer is None:
        print("No solution.")
        return
    print("Solution:")
    for row in answer:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
