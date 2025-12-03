"""
This is the third challenge of Advent Code 2025.
"""
"""
Part 1:
You need to restart an electric escalatror to go down through the 
north pole base. The escalator have a series of batery cells, each 
batery beein a nimber from 0 to 9. You have a list of the batery cells
in the input file an you need to find, for each cell, the max two 
digits number that can be formed with the digits of the cell number.
It's important to note that the digits must be in the same order as
they appear in the cell number. You can't rearrange them.
Once you find the max two digits number for each cell, you need to
sum all the max two digits numbers and that will be the result.
"""

result = 0
data = []

with open("input.txt", "r") as file:
    data = file.readlines()
    
# Read each line in the input file
for line in data:
    # For each line, find the max two digits number
    digit1 = 0
    digit2 = 0
    line = line.strip()
    # Iterate through each digit in the line
    for i in range(len(line)):
        # Check if the current digit is greater than digit1 and is not the last index
        if int(line[i]) > digit1 and i < (len(line) - 1):
            digit1 = int(line[i])
            digit2 = 0
        else:   # Check if the current digit is greater than digit2 or digit2 is 0 which means it hasn't been set yet
            if int(line[i]) > digit2 or digit2 == 0:
                digit2 = int(line[i])
    # Add the max two digits number to the result
    result += (digit1 * 10 + digit2)
        
print("The result for part 1 is:", result)

"""
Part 2:
It seems that the escalator needs a bit more power to restart. You need to find, for each batery cell,
the max twelve digits number that can be formed with the digits of the cell number. Again, the digits 
must be in the same order as they appear in the cell number. You can't rearrange them. Once you find
the max twelve digits number for each cell, you need to sum all the max twelve digits numbers and that
will be the result.
"""