# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
pin = ""

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

pin = int(input("four digit PIN: "))




if pin[0] == pin[3] and pin[1] == pin[2]:
    print("the PIN cannot have all four numbers the same")



