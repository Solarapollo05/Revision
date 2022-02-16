# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------

CM_IN_INCH = 2.54

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# ===> Change the identifier x to a more meaningful name

height = 0

# ===> fix the syntax error in line 15
choice = ""

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> convert the user's input to a floating point number before assignment

height = input("Enter your height in metres: ")

# ===> display a suitable question to the user for their choice of 'cm' or 'inch'
print("Choose  centimetres, or inches\n")

# ===> accept the user's input
choice = input(" >  ")

# ===> fix the syntax error in line 32
if choice == "inch":

# ===> replace 2.54 with a constant
# ===> make two uses of white space to aid readability in the next line
    result=height * 100 / CM_IN_INCH

    print(result, "inches")

# ===> if the user enters 'cm' then
#      perform the calculation to convert metres to centimetres
# ===> output the resulting number of centimetres followed by 'centimetres'
elif choice == "cm":
    result = height * 100
    
    print(result, "centimetres")


