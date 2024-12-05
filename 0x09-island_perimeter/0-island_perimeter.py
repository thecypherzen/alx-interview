#!/usr/bin/python3
"""Island Perimeter Algorithm
"""


def island_perimeter(grid):
    """Calculates Perimeter of Island given grid

    Params:
     - grid(list[list]): list of lists of integers such that:
       - 0 represents water
       - 1 represents land
       - Each cell is square, with a side length of 1
       - Cells are connected horizontally/vertically (not
         diagonally).
       - `grid` is rectangular, with its width and height not
          exceeding 100
     - The grid is completely surrounded by water
     - There is only one island (or nothing).
     - The island doesn’t have “lakes” (water inside that isn’t
       connected to the water surrounding the island).
    Example:
    [
      [0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]
    ] >> 12.
    """
    perimeter = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col]:
                perimeter += 1 if not grid[row-1][col] else 0
                perimeter += 1 if not grid[row+1][col] else 0
                perimeter += 1 if not grid[row][col+1] else 0
                perimeter += 1 if not grid[row][col-1] else 0
    return perimeter
