#Edulito practice exams 2 1CP2/02 Q04a

# ----- Globals -----
age = int()
human_age = int()

# ----- Main -----

age = int(input("What is your dog's age?"))

if age == 12:
    human_age = int(1)
else:
    human_age = 24 + (4 * age - 2)

print("Your dog's age in human years is", human_age)



