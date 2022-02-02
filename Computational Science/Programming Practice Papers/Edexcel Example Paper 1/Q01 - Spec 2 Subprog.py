# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
WIT = "wit"
FOOL = "fool"

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
start = 0
end = 0
location = 0

# =====> Complete the line to create a one-dimensional data structure
#        (list) with 9 integers between 0 and 100, inclusive, in any order
myList =

# ====> Initialise mySentence to this quote: Better a witty fool than a foolish wit
mySentence =

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def showList (inList):
    outString = ""

    for item in inList:
        # =====> Fix the type error
        outString = outString + item + " "
    print (outString)

def findLocation (inString, inTarget, inStart, inEnd):
    location = -1

    location = inString.find (inTarget, inStart, inEnd)

# =====> Fix the indentation error
return (location)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Fix the name error
shwList (myList)

# =====> Complete the line with a built-in function to find the
#        length of mySentence
end = mySentence)

# =====> Fix the syntax error
while (location != -1)
    location = findLocation (mySentence, FOOL, start, end)

    # =====> Complete the line with the keyword for selection
    (location != -1):
        # =====> Fix the syntax error
        print (FOOL + " found at location: " + str location)
        # =====> Fix the logic error
        start = location - 1