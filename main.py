# Basic Console Sudoku Solver

def findEmptySpace(board):
    """
    Find the next empty cell (number == 0) on the puzzle board
    :param board: A list of 9 lists each with 9 spaces representing a sudoku board
    :return: tuple (r,c) r-row, c-column, None if not empty space is found
    """
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return tuple([r, c])
    # Return None
    return None


def valid(board, number, position):
    """
    Determines if the number is valid to put at the given position
    :param board: A list of 9 lists each with 9 spaces representing a sudoku board
    :param number: int [1,9]
    :param position: tuple (r,c) r-row, c-column
    :return: Boolean, True if valid, false otherwise
    """
    # Get positions from tuple
    row, col = position

    # row check
    for i in range(len(board[0])):
        if board[row][i] == number and row != i:
            return False
    # column check
    for i in range(len(board)):
        if board[i][col] == number and col != i:
            return False

    # 3x3 box check
    boxStartRow = (row // 3) * 3
    boxStartCol = (col // 3) * 3
    for i in range(boxStartRow, boxStartRow + 3):
        for j in range(boxStartCol, boxStartCol + 3):
            if board[i][j] == number and row != i and col != j:
                return False
    return True


def printBoardConsole(board):
    """
    prints the board on the console
    :param board: A list of 9 lists each with 9 spaces representing a sudoku board
    :return: void
    """
    if findEmptySpace(board) is None:
        print("Finished Sudoku!!!")
    else:
        print("Unsolved Sudoku")
    for i in range(len(board)):
        if i % 3 == 0:
            print("-------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("\b|", end="")

            print(str(board[i][j]) + " ", end="")
        print("\b|")
    print("-------------------")


def solve_board(board):
    """
    Solve the sudoku puzzle using recursion and backtracking
    :param board:A list of 9 lists each with 9 spaces representing a sudoku board
    :return: Boolean, True if the puzzle is solved, False otherwise
    """
    emptyFound = findEmptySpace(board)
    if emptyFound is None:
        # Puzzle solved
        return True
    else:
        row, col = emptyFound

    for i in range(1,10):
        # If the value and position is valid, put the value on the board
        if valid(board, i, emptyFound):
            board[row][col] = i

        # If the board is solved, return True
            if solve_board(board):
                return True
        # If the board cannot be solved, restore the board
            board[row][col] = 0
        # Not solvable
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
             [6, 0, 0, 0, 7, 5, 0, 0, 9],
             [0, 0, 0, 6, 0, 1, 0, 7, 8],
             [0, 0, 7, 0, 4, 0, 2, 6, 0],
             [0, 0, 1, 0, 5, 0, 9, 3, 0],
             [9, 0, 4, 0, 6, 0, 0, 0, 5],
             [0, 7, 0, 3, 0, 0, 0, 1, 2],
             [1, 2, 0, 0, 0, 7, 4, 0, 0],
             [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    printBoardConsole(board)
    solve_board(board)
    printBoardConsole(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
