def is_valid_move(grid, row, col, num):
    # Check if the number is already present in the row
    if num in grid[row]:
        return False

    # Check if the number is already present in the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the number is already present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack

    return False  # No solution found

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def input_grid():
    print("Enter the unsolved Sudoku puzzle row by row, with each row separated by spaces.")
    print("Use numbers from 1 to 9 for filled cells and 0 for empty cells.")
    grid = []
    for i in range(9):
        while True:
            row_input = input(f"Enter row {i + 1}: ")
            row = []
            for char in row_input.split():
                if not char.isdigit() or not (0 <= int(char) <= 9):
                    print("Invalid input. Please use numbers from 0 to 9.")
                    break
                row.append(int(char))
            else:
                if len(row) != 9:
                    print("Invalid input. Each row must contain exactly 9 numbers.")
                else:
                    grid.append(row)
                    break
    return grid

if __name__ == "__main__":
    puzzle = input_grid()

    if puzzle:
        if solve_sudoku(puzzle):
            print("Sudoku puzzle solved successfully:")
            print_grid(puzzle)
        else:
            print("No solution exists for this Sudoku puzzle.")
    else:
        print("Invalid input. Exiting program.")
