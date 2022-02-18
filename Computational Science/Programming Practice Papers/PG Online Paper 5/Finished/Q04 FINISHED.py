# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", \
          "SEP", "OCT", "NOV", "DEC"]   #Do not move this line
months31 = ["JAN", "MAR", "MAY", "JUL", "AUG", \
            "OCT", "DEC"]               #Do not move this line
months30 = ["APR", "JUN", "SEP", "NOV"] #Do not move this line

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Put the lines into the correct order to solve the problem.
# A user enters a month. If the user enters 'Feb', the program asks
# whether the year is a leap year (as 'y' or 'n').
# The program will then state the number of days that are in that
# month according to the following table:
# Jan 31
# Feb 28 or 29 on leap years
# Mar 31
# Apr 30
# May 31
# Jun 30
# Jul 31
# Aug 31
# Sep 30
# Oct 31
# Nov 30
# Dec 31
# For example:
# Input Month: Feb
# Input leap year: y
# Output: 29 days
# ---
# Input Month: Mar
# Output: 31 days

validMonth = False


while not validMonth:
    month = input("Enter the first three letters of the month: ")
    month = month.upper()
    if month in months:
        validMonth = True

if month in months30:
    print("30 days")

elif month in months31:
    print("31 days")

else:
    leapYear = input("Enter if the year is a leap year ('y' or 'n'): ")
    if leapYear == 'y':
        print("28 days")
    else:
        print("29 days")















    
