# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
name = ""
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
print("Enter your name")
name = input(" >     ")

if name == "":
    print("Name cannot be blank")
elif len(name) <3:
    print("Name cannot be less than 3 characters")
elif len(name) >20:
    print("Name cannot be longer than 20 characters")
else:
    print("All checks passed")