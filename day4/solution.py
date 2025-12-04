"""
This is the fourth challenge of Advent Code 2025.
"""
"""
Part 1:
You need to help the Elves optimize the work of the forklifts in the 
printing department so they can free up time to break through a wall 
and reach the cafeteria. The department has a large grid representing 
the positions of paper rolls (@). A forklift can only access a roll 
if there are fewer than four rolls in the eight adjacent positions 
(orthogonal and diagonal). Your task is to analyze the grid and 
determine how many rolls of paper are accessible under this rule.
"""

# Function to check if a roll of paper is accessible
def is_accessible(row, col, grid, max):
    # Directions for the 8 adjacent cells
    directions = [ (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
    
    count = 0    
    # Check all adjacent cells
    for dr, dc in directions:
        # Calculate the position of the adjacent cell
        r, c = row + dr, col + dc
        # Ensure the position is within bounds
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            # Count if there's a roll of paper
            if grid[r][c] == '@':
                count += 1
    # A roll is accessible if fewer than 'max' adjacent rolls are found
    # Note that if the rol is in the corner or edge, it naturally has fewer adjacent rolls     
    return count < max

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]
    
accessible_count = 0

# Iterate through each cell in the grid
for r in range(len(grid)):
    # Check each cell in the grid
    for c in range(len(grid[0])):
        # If it's a roll of paper, check accessibility
        if grid[r][c] == '@' and is_accessible(r, c, grid, 4):
            accessible_count += 1
            
print("Part 1: Accessible rolls of paper:", accessible_count)
    
"""
Part 2:
Now,you need to help the Elves to access more rolls of paper by
removing the visited rolls from the grid. Each time a roll is removed,
the accessibility of the surrounding rolls may change. Your task is to
determine how many rolls of paper can be removed in total by repeatedly
removing accessible rolls until no more can be removed.
"""

changes = True
removable_count = 0

# Iteratively remove accessible rolls until no more can be removed
while changes:
    changes = False
    # Check each cell in the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # If it's a roll of paper, check accessibility
            if grid[r][c] == '@' and is_accessible(r, c, grid, 4):
                # Remove the roll of paper, count it, and mark that a change was made to continue the loop
                grid[r][c] = '.'
                changes = True
                removable_count += 1

print("Part 2: Total removable rolls of paper:", removable_count)