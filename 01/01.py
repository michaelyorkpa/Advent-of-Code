#Declare variables
ielf_list = []
new_elf = 0
max_calories = 0
ielf_list.append(0)

# Open Text file determine whether each line is a number or \n
# If \n increase the elf count
# During elf count increase, check to see what the previous elf's
# calorie count was. If it's higher than current max calorie count, record
# the elf number in highest_elf and calorie count in max_calories
with open('data.txt') as elf_file:
    for line in elf_file:
        if line == "\n": # Is it a blank line?
            new_elf += 1 # Increase the elf count
            ielf_list.append(0) # Add a new elf to the list
            if ielf_list[new_elf-1] > max_calories: # Check the previous elf to see if it
                highest_elf = new_elf - 1 # Record which elf is the highest
                max_calories = ielf_list[new_elf-1] # Record the highest calorie amount
        else:
            line = int(line.strip('\n')) # Strip the line of \n and convert to an integer
            ielf_list[new_elf] += line # Add the newly created integer to the previous value

# Close the file
elf_file.close()

# Print the answer
print("Elf number "+str(highest_elf)+" is carrying "+str(max_calories)+" calories.",end="\n")