# Correct Answer: 16862
# Declare variables
myscore = 0
myturn = 0
opponent = 0

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
            result = "Loss"
        if line[2] == "Y":
            result = "Draw"
        if line[2] == "Z":
            result = "Win"

        # Draw scoring
        if result == "Draw":
            myturn = opponent
            myscore += myturn+3

        # Win Scoring
        if result == "Win":
            if opponent == 1:
                myturn = 2
            if opponent == 2:
                myturn = 3
            if opponent == 3:
                myturn = 1
            myscore += myturn+6

        # Loss Scoring
        if result == "Loss":
            if opponent == 1:
                myturn = 3
            if opponent == 2:
                myturn = 1
            if opponent == 3:
                myturn = 2
            myscore += myturn

        if opponent == 1: 
            opponentword = "Rock"
        if opponent == 2:
            opponentword = "Paper"
        if opponent == 3:
            opponentword = "Scissors"

        if myturn == 1:
            myword = "Rock"
        if myturn == 2:
            myword = "Paper"
        if myturn == 3:
            myword = "Scissors"

        print("Opponent: "+str(opponent)+" - Me: "+str(myturn)+" - This round was a "+result+". "+str(myscore),end="\n")


print ("Total Score: "+str(myscore),end="\n")