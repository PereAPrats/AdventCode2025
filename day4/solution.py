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
def is_accessible(row, col, grid, max):
    direcctions = [ (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
    
    coun = 0
    
    for dr, dc in direcctions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == '@':
                coun += 1
                
    return coun < max

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]
    
accessible_count = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
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


while changes:
    changes = False
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@' and is_accessible(r, c, grid, 4):
                grid[r][c] = '.'
                changes = True
                removable_count += 1

print("Part 2: Total removable rolls of paper:", removable_count)