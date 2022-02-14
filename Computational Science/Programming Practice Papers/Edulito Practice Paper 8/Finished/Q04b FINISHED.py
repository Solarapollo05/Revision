#Edulito practice exams 2 1CP2/02 Q04b

#Function
def dog_years(age):
    if age == 12:
        human_age = int(1)
    else:
        human_age = 24 + (4 * age - 2)
    return human_age

#Main Program

age = int(input("What is your dog's age?"))

human_age = dog_years(age)

print("Your dog is", human_age, "years old in human years.")
          


