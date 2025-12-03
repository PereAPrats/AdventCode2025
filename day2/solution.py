"""
This is the second challenge of Advent Code 2025.
"""
"""
Part 1:
The challenge is about identifying haw many product codes are invalid
after a young elf played with the warehouse inventory system.
The codes are inside the input file, they are ranges of numbers separated
by commas.
A wrong code is defined as a code with to sequence of digits repeated, for
example 55, 123123 or 1188511885.
Once processed all the codes, the program returns the sum of all invalid ones.
"""
import re

with open("input.txt", "r") as file:
    data = file.read().strip()

ranges = re.split(r',\s*', data)
invalid_sum = 0

for i in ranges:
    izq, der = i.split('-')
    for j in range(int(izq), int(der)):
        if (len(str(j)) % 2) != 0:
            continue
        if str(j)[:len(str(j))//2] == str(j)[len(str(j))//2:]:
            invalid_sum += j

print(f"Part 1: The sum of all invalid product codes is {invalid_sum}.")

"""
Part 2:
Now, an ID is invalid if it is made only of some sequence of digits repeated at
least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 
(12 five times), and 1111111 (1 seven times) are all invalid IDs.
"""

invaliS_sum = 0

# Regular expression to match a sequence of digits repeated at least twice
# r'^(\d+?)\1+$' Explanation:
# ^ asserts position at start of the string
# (\d+?) captures one or more digits (non-greedy) as group 1
# \1+ matches the same digits as captured in group 1, one or more times
# $ asserts position at the end of the string
patron = re.compile(r'^(\d+?)\1+$')

def es_invalido(num) -> bool:
    return patron.fullmatch(str(num)) is not None

for i in ranges:
    izq, der = i.split('-')
    for j in range(int(izq), int(der)):
        if es_invalido(j):
            invaliS_sum += j
            
print(f"Part 2: The sum of all invalid product codes is {invaliS_sum}.")

    