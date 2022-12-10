# Correct Answer: 11475
# Declare variables
myscore = 0

# Open text file
with open('data.txt') as rps_file:
    for line in rps_file:
        #line = line.strip('\n')
        
        # Register opponent's value
        if line[0] == "A":
            opponent = 1 # Rock
        if line[0] == "B":
            opponent = 2 # Paper
        if line[0] == "C":
            opponent = 3 # Scissors
        # Register my value
        if line[2] == "X":
            myturn = 1 # Rock
        if line[2] == "Y":
            myturn = 2 # Paper
        if line[2] == "Z":
            myturn = 3 # Scissors

        # Draw scoring
        if opponent == myturn:
            myscore += myturn + 3
            result = "Draw"

        # Opponent Rock
        if opponent == 1:
            if myturn == 2: # Player Paper
                result = "Win"
            if myturn == 3: # Player Scissors
                result = "Lose"

        # Opponent Paper
        if opponent == 2:
            if myturn == 1: # Player Rock
                result = "Lose"
            if myturn == 3: # Player Scissors
                result = "Win"
        
        # Opponent Scissors
        if opponent == 3:
            if myturn == 1:
                result = "Win" # Player Rock
            if myturn == 2: # Player Paper
                result = "Lose"

        if result == "Win":
            myscore += myturn+6
        
        if result == "Lose":
            myscore += myturn

        print("Opponent: "+line[0]+"- Me: "+line[2]+" - This round was a "+result+".",end="\n")

print ("Total Score: "+str(myscore),end="\n")