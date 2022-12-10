# Correct Answer: 433
# 235 too low; 469 too high
# Declare Variables
section = []
partner1 = []
partner2 = []
i = 0
within = 0

# Open file
with open('data.txt') as sect_file:
    for line in sect_file:
        line = line.strip('\n') # Strip the new line char
        section.append(line.split(",")) # Split the line into the paired elves
        partner1.append(section[i][0].split("-")) # Split the sections into partner 1
        partner2.append(section[i][1].split("-")) # Split the sections into partner 2

        # Test if partner's are within each other's sections
        if int(partner1[i][0]) >= int(partner2[i][0]) and int(partner1[i][1]) <= int(partner2[i][1]):
            within += 1
            print("Partner pair: "+str(i)+" Partner 1: "+section[i][0]+" - Partner 2: "+section[i][1],end="\n") 
        elif int(partner2[i][0]) >= int(partner1[i][0]) and int(partner2[i][1]) <= int(partner1[i][1]):
            within += 1
            print("Partner pair: "+str(i)+" Partner 1: "+section[i][0]+" - Partner 2: "+section[i][1],end="\n") 

        i += 1 # Increase the partner list variable 
        
print("Total sections within sections: "+str(within))