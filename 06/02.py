# Correct answer: 3051
with open('data.txt') as com_file:
    for line in com_file:
        line = line.strip('\n')

        for group in range(0,len(line)):
            # set breaks the string into individual unique characters
            # len counts the total unique characters in the string
            test = len(set(line[group:group+14])) 
            # if the unique characters in the string == 4, print the answer, break the loop
            if test == 14: print("The answer is "+str(group+14)); break
