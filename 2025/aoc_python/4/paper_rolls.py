import os
import logging

def find_rolls(grid):
    roll_coordinates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                roll_coordinates.append((i, j))
    return roll_coordinates

# jth column, ith row
#    (j-1,i-1)(j,i-1)(j+1,i-1)
#     (j-1,i)  (j,i)  (j+1,i)
#    (j-1,i+1)(j,i+1)(j+1,i+1)
# If >= 4 of the indices surrounding (j,i) are occupied, the "paper roll" cannot be moved
def analyze_rolls(roll_coordinates, grid):
    accessible_coordinates = []
    for c in roll_coordinates:
        tl = (c[0]-1,c[1]-1)
        tm = (c[0],c[1]-1)
        tr = (c[0]+1,c[1]-1)
        ml = (c[0]-1,c[1])
        mr = (c[0]+1,c[1])
        bl = (c[0]-1,c[1]+1)
        bm = (c[0],c[1]+1)
        br = (c[0]+1,c[1]+1)
        adjacent_coords = [tl, tm, tr, ml, mr, bl, bm, br]
        sides_surrounded = 0
        for ac in adjacent_coords:
            # This condition checks our boundaries, grid indices less than zero or equal to the
            # length or width of the grid are not valid
            if ac[0] >= 0 and ac[1] >= 0 and ac[0] < len(grid[0]) and ac[1] < len(grid):
                if grid[ac[0]][ac[1]] == '@':
                    sides_surrounded = sides_surrounded + 1
        if sides_surrounded < 4:
            accessible_coordinates.append(c)

    return accessible_coordinates, len(accessible_coordinates)

def remove_rolls(accessible_coordinates, grid):
    modified_grid = grid
    for ac in accessible_coordinates:
        modified_grid[ac[0]][ac[1]] = 'X'

    return modified_grid

# This seems like it's slower than it should be
def recursively_remove(grid):
    # Find all of the rolls
    roll_coordinates = find_rolls(grid)
    # Find the ones we can currently remove
    accessible_coordinates, num_accessible_rolls = analyze_rolls(roll_coordinates, grid)
    # Remove the rolls
    modified_grid = remove_rolls(accessible_coordinates, grid)
    # We have no more count to add if no more are accesible, so return 0
    if num_accessible_rolls == 0:
        return 0
    else:
        # Otherwise, add the current number removed and keep going with the updated grid
        return num_accessible_rolls + recursively_remove(modified_grid)



def main():
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/./input.txt', 'r') as f:
        grid = []
        for line in f:
            # Make our string into a list so it's mutable
            grid.append(list(line.strip()))
        roll_coordinates = find_rolls(grid)
        _, num_accessible_rolls = analyze_rolls(roll_coordinates, grid)

        logging.info(f'Number of accessible rolls: {num_accessible_rolls}')
        # Part 2
        total_removable = recursively_remove(grid)
        logging.info(f'Total removable rolls: {total_removable}')
    


if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.DEBUG)
    main()