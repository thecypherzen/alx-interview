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
      [0, 1, 0, 0, 0, 0],
      [0, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0]
    ] >> 12.
    """

    visited = set()
    cols, rows = len(grid[0]), len(grid)
    row_edges, col_edges = (1, rows - 2), (1, cols - 2)

    # helper func to cal perim of each cell
    def perimeter_of(i, j):
        """search for perimeter cells
        """
        if (i, j) in visited:
            return 0
        # keep track of each cell and skip cells out of bounds
        # or with water(0)
        visited.add((i, j))
        if i < row_edges[0] or i > row_edges[1] or \
           j < col_edges[0] or j > col_edges[1] or \
           not grid[i][j]:
            return 0
        # cal perim of cell and pick next cell with land(1)
        perimeter, points = 0, [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]
        next_point = None
        for point in points:
            if grid[point[0]][point[1]] and point not in visited:
                next_point = point
            if not grid[point[0]][point[1]]:
                perimeter += 1
        # add perim of next land to current or return
        if next_point:
            perimeter += perimeter_of(*next_point)
        return perimeter

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col]:
                return perimeter_of(row, col)
    return 0
