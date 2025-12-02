"""
This is the first challenge of Advent Code 2025.
"""
"""
Part 1:
The challenge is enter to a secret entrance at the North pole
by finding the password hidden in the input file.
The input document contains a sequence of rotations to enter on
a rotating dial lock mechanism. The dial has numbers from 0 to 99.
Each rotation have the format: <Direction><Steps> with Direction being
either 'L' for left (counter-clockwise) or 'R' for right (clockwise)
and Steps being the number of steps to rotate the dial.
The dial starts at number 50.
The password is the number of times the dial hit the number 0 after 
processing all the rotations in the input file.

"""

startNumber = 50
currentNumber = startNumber
zeroHits = 0

with open("input.txt", "r") as file:
    for line in file:
        direction = line[0]
        steps = int(line[1:])
        
        if direction == 'L':
            currentNumber = (currentNumber - steps) % 100
        elif direction == 'R':
            currentNumber = (currentNumber + steps) % 100
        
        if currentNumber == 0:
            zeroHits += 1
    
print(f"The password to enter the secret entrance is: {zeroHits}")

"""

Part 2:
The password seems correct but the entrance is still locked.
After doing a snowman in the snow, a hidden message appears.
It seems that te password use the method 0x434C49434B, wich 
means that you're actually supposed to count the number of 
times any click causes the dial to point at 0, regardless 
of whether it happens during a rotation or at the end of one.

So let's modify the code to count every time the dial passes through 0.

"""

startNumber = 50
currentNumber = startNumber
zeroHits = 0

with open("input.txt", "r") as file:
    for line in file:
        direction = line[0]
        steps = int(line[1:])
        
        if direction == 'L':
            for step in range(steps):
                currentNumber = (currentNumber - 1) % 100
                if currentNumber == 0:
                    zeroHits += 1
                
        elif direction == 'R':
            for step in range(steps):
                currentNumber = (currentNumber + 1) % 100
                if currentNumber == 0:
                    zeroHits += 1
            
print(f"The updated password to enter the secret entrance is: {zeroHits}")