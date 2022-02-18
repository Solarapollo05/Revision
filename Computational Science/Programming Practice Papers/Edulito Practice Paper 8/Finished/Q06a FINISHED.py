#Edulito practice exams 2 1CP2/02 Q06a
print("Enter the names of the teams: \n")

team1 = input("Enter the first team's name\n >   ")
team2 = input("Enter the first team's name\n >   ")

score1 = int(input(f"What score did {team1} get?\n >   "))
score2= int(input(f"What score did {team2} get?\n >   "))

if score1 == score2:
    print("Draw!")
elif score1 > score2:
    print(f"{team1} has won.")
else:
    print(f"{team2} has won.")
