# -------------------------------------------------------------------
# Libraries
# -------------------------------------------------------------------
# =====> Import a needed library
import math
# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
SELVEDGE_WIDTH = 8               # The frayed edge on the side
# =====> Create a constant for the width of the fabric
#        and set it to 147
FABRIC_WIDTH = 147

# --------------------------------------------- ----------------------
# Global variables
# -------------------------------------------------------------------
poleLength = 0
fullnessRatio = 0.0
numberWidths = 0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def isValidFullness (pFullness):
    # =====> Complete the code for this subprogram
    if pFullness == 2 or pFullness == 2.5 or pFullness == 3:
        return True
    else:
        return False
# =====> Complete the definition for this subprogram
def calcNumberOfWidths (pPoleLength, pFullnessRatio):
    numWidths = 0                   # Initialise
    usableFabricWidth = 0

    # =====> Calculate usable fabric width
    numberWidths = FABRIC_WIDTH - SELVEDGE_WIDTH
    # =====> Calculate number of fabric widths required
    usableFabricWidth = 
    return (numWidths)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
poleLength = int (input ("Enter the pole width (120, 180, 240): "))

# =====> Accept the fullness ratio from the user
fullnessRatio = float(input("Enter the Fullness Ratio:  "))

if (isValidFullness (fullnessRatio)):
    # =====> Call the subprogram to calculate number of widths
    numberWidths = calcNumberOfWidths(poleLength, fullnessRatio) 
    print ("Number of widths required is " + str (numberWidths))
else:
    print ("Invalid fullness ratio")

