# Correct Answer: 2342
total = 0
item = []
with open('data.txt') as ruck_file:
    for line in ruck_file:
        line = line.strip('\n') # strip the new line char
        item.append(line) # Put each string into a list

for badges in range(0, int(len(item)), 3):
    # Parse the three strings for the matching character
    for i in range(0, len(item[badges])): # Loop through 1
        for j in range(0, len(item[badges+1])): # Loop through 2
            if item[badges][i] == item[badges+1][j]: # If there's a match between 1 & 2, start looping 3
                for char in range(0, len(item[badges+2])): # If there's a match between 1, 2, & 3 set the match variable
                    if item[badges+1][j] == item[badges+2][char]:
                        match = item[badges+2][char]
                        break

    # Prioritize badges
    if match == "a":total += 1
    if match == "b":total += 2
    if match == "c":total += 3
    if match == "d":total += 4
    if match == "e":total += 5
    if match == "f":total += 6
    if match == "g":total += 7
    if match == "h":total += 8
    if match == "i":total += 9
    if match == "j":total += 10
    if match == "k":total += 11
    if match == "l":total += 12
    if match == "m":total += 13
    if match == "n":total += 14
    if match == "o":total += 15
    if match == "p":total += 16
    if match == "q":total += 17
    if match == "r":total += 18
    if match == "s":total += 19
    if match == "t":total += 20
    if match == "u":total += 21
    if match == "v":total += 22
    if match == "w":total += 23
    if match == "x":total += 24
    if match == "y":total += 25
    if match == "z":total += 26
    if match == "A":total += 27
    if match == "B":total += 28
    if match == "C":total += 29
    if match == "D":total += 30
    if match == "E":total += 31
    if match == "F":total += 32
    if match == "G":total += 33
    if match == "H":total += 34
    if match == "I":total += 35
    if match == "J":total += 36
    if match == "K":total += 37
    if match == "L":total += 38
    if match == "M":total += 39
    if match == "N":total += 40
    if match == "O":total += 41
    if match == "P":total += 42
    if match == "Q":total += 43
    if match == "R":total += 44
    if match == "S":total += 45
    if match == "T":total += 46
    if match == "U":total += 47
    if match == "V":total += 48
    if match == "W":total += 49
    if match == "X":total += 50
    if match == "Y":total += 51
    if match == "Z":total += 52

    badges += 3

print("Total Badge Priorities: "+str(total))