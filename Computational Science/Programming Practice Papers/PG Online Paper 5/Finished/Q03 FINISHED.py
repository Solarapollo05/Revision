# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
pin = ""

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

pin = str(input("four digit PIN: "))

if len(pin) != 4:
    print("Invalid input.")


elif pin[0] == pin[3] or pin[1] == pin[2]:
    print("the PIN cannot have all four numbers the same")

else:
    print("New PIN accepted.")


