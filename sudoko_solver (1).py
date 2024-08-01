def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def is_valid(board, num, pos):
    # Check row
    for c in range(9):
        if board[pos[0]][c] == num and c != pos[1]:
            return False
    # Check column
    for r in range(9):
        if board[r][pos[1]] == num and r != pos[0]:
            return False
    # Check 3x3 box
    box_r = pos[0] // 3 * 3
    box_c = pos[1] // 3 * 3
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if board[r][c] == num and (r, c) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Example Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku puzzle:")
print_board(board)
print("\nSolving...\n")

if solve(board):
    print("Sudoku solved:")
    print_board(board)
else:
    print("No solution exists.")
