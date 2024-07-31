#!/usr/bin/python3
""" DOC """


def island_perimeter(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    def is_water_or_out_of_bounds(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return True
        return grid[r][c] == 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four possible directions
                if is_water_or_out_of_bounds(r - 1, c):  # Up
                    perimeter += 1
                if is_water_or_out_of_bounds(r + 1, c):  # Down
                    perimeter += 1
                if is_water_or_out_of_bounds(r, c - 1):  # Left
                    perimeter += 1
                if is_water_or_out_of_bounds(r, c + 1):  # Right
                    perimeter += 1

    return perimeter
