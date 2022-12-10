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
        if line == "\n":
            new_elf += 1
            ielf_list.append(0)
            if ielf_list[new_elf-1] > max_calories:
                highest_elf = new_elf - 1
                max_calories = ielf_list[new_elf-1]
        else:
            line = int(line.strip('\n'))
            ielf_list[new_elf] += line

# Close the file
elf_file.close()

second_elf = 0
second_calories = 0
for elf in range(0, len(ielf_list)):
    if ielf_list[elf] > second_calories and ielf_list[elf] < max_calories:
        second_elf = elf
        second_calories = ielf_list[elf]

third_elf = 0
third_calories = 0
for elf in range(0, len(ielf_list)):
    if ielf_list[elf] > third_calories and ielf_list[elf] < second_calories:
        third_elf = elf
        third_calories = ielf_list[elf]

# Print the answer
print("Elf number "+str(highest_elf)+" is carrying "+str(max_calories)+" calories.",end="\n")
print("Elf number "+str(second_elf)+" is carrying "+str(second_calories)+" calories.",end="\n")
print("Elf number "+str(third_elf)+" is carrying "+str(third_calories)+" calories.",end="\n")
print("Total calories of top 3 elves:"+str(max_calories+second_calories+third_calories),end="\n")