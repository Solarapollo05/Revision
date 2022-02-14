#Edulito practice exams 2 1CP2/02 Q02
print("Fortune Teller Game")

name = input("First let's find out who you are, what's your name?  ")
print("ummh",name,"......that is a very interesting name")
print("now",name,"it's time to read your fortune") 
import random
x = random.randint(1,6) # Generates a random number between 1 and 6

if x == 1:
    print("let me think....it's getting clearer")
    print(name,"You will have 4 children"))
elif x == 2:
    print("yes,yes....it's becoming very clearer")
    print(name,"you will be a millionaire before the age of 30")
elif x == 3:
    print("ummmhh....I don't believe it")
    print(name,"you will be a leader and people will listen carefully to you.")
elif x == 4:
    print("Can this be true!!!")
    print(name,"I see you taking part in the Olympics")
elif x == 5:
    print("can this be!!!")
    print(name,"you will be happy and healthy and live beyond 100")
elif x == 6:
    print("what! it is too hazy I must think .....")
    print(name,"you will have your own TV series")
elif x == 7:
    print("{Something funny}")
