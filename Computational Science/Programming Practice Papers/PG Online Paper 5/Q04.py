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



if leapYear == 'y':
month = month.upper()
leapYear = input("Enter if the year is a leap year ('y' or 'n'): ")
validMonth = False
if month in months30:
if month in months:
print("30 days")
month = input("Enter the first three letters of the month: ")
elif month in months31:
while not validMonth:
print("28 days")
else:
validMonth = True
else:
print("31 days")
print("29 days")




    
