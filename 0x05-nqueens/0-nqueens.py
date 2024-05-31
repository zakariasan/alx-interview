#!/usr/bin/env python3
""" n queen """
import sys


def print_usage():
    """Prints usage message"""
    print("Usage: nqueens N")


def print_error_message(message):
    """Prints error message and exits with status 1"""
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """Checks if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """Uses backtracking to solve the N queens problem"""
    if col >= len(board):
        print_board(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0

    return res


def print_board(board):
    """Prints the board in the required format"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_message("N must be a number")

    if N < 4:
        print_error_message("N must be at least 4")

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
