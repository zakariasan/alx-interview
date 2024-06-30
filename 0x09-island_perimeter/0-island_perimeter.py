#!/usr/bin/python3
""" island perimeter """


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Top
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1  # Bottom
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Left
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1  # Right

    return perimeter
