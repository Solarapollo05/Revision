#Edulito practice exams 2 1CP2/02 Q06b
results=[]
new_entry=[]
entry="Y"

while entry=="Y":

    team1 = input("Enter the first team's name\n >   ")
    team2 = input("Enter the first team's name\n >   ")

    score1 = int(input(f"What score did {team1} get?\n >   "))
    score2= int(input(f"What score did {team2} get?\n >   "))       

    new_entry.append(team1)
    new_entry.append(score1)
    new_entry.append(team2)
    new_entry.append(score2)
    
    results.append(new_entry)
    entry = input("Would you like to enter another result? ")

print(results)
