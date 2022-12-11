# Correct Answer: NTWZZWHFV
# Initialize the stack
row = []
inst = []
i = 0

# Open the crate stack and load it an array
print("Opening the file...")
with open('init-stack.txt') as stack_File:
    for line in stack_File:
        line = line.strip('\n')
        row.append(line)
print("Done.\n")

# Figure out number of columns to slice the data
print("Figure out how many columns there are...")
numCol = len(row[i])/4
numColP = (len(row[i])+1)/4
if numCol == int(numCol):
    numCol = int(numCol)
elif numColP == int(numColP):
    numCol = int(numColP)
else:
    numCol = int((len(row[i])-1)/4)
print("Done.\n")

# Initialize the column variable
print("Initialize the 2d column list... ")
col = [[] for list in range(numCol)]
print("Done.\n")

# Run the rows through backwards
print("Build the columns... ")
print(len(row))
for i in range(len(row)-1, -1, -1):
    start = 0
    end = 3
    for crate in range(0, numCol):
        if row[i][start:end] != "   ": # If it's blank, skip it!
            col[crate].append(row[i][start:end]) # If not, load it into row!
        start += 4 # Increase the variables by 4 to move to the next column
        end += 4
print("Done.\n")

# Open the data file
# Strip it down to the values
# Load the values into the instructions array
print("Opening the instructions file and building the instructions list...")
with open('data.txt') as inst_file:
    for line in inst_file:
        line = line.strip('\n')
        line = line.replace("move ","")
        line = line.replace(" from", "")
        line = line.replace(" to", "")
        inst.append(line.split(" "))
print("Done.\n")

# Process the instructions list against the columns list
print("Process the instructions...")
for i in range(0,len(inst)):
    howMany = -abs(int(inst[i][0])) # How many crates to move
    whichCol = int(inst[i][1])-1 # From Column
    newCol = int(inst[i][2])-1 # To column

    # Debug
    #for j in range(0,len(col)):
    #    print(col[j],end='\n')

    #print("Move "+inst[i][0]+" From "+inst[i][1]+" To "+inst[i][2])

    #debug = input("Press Enter to Continue: ")

    for doMove in range(0, abs(howMany)):
        moveIt = col[whichCol].pop()
        col[newCol].append(moveIt)
print("Done.\n")

#debug = input("Press Enter to Continue: ")

answer = col[0].pop()+col[1].pop()+col[2].pop()+col[3].pop()+col[4].pop()+col[5].pop()+col[6].pop()+col[7].pop()+col[8].pop()
answer = answer.replace('[',"")
answer = answer.replace(']',"")

print(answer)
