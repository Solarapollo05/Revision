# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
monthlySales = [34000, 22000, 24000, 37000, 42000, 41000, \
                58000, 49000, 22000, 16000, 12000, 30000]
averageSales = 0.0


# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

# ===> Add one parameter inside the brackets
def calcTotal(               ):
    print("The monthly sales are:", salesList)

    totalSales = 0

    for sale in salesList:
        totalSales = totalSales + sale

    print("The total sales are:", totalSales)

    # ===> Complete the calculation for the average each sale in salesList
    
    

    print("The average sales are:", average)

    # ===> Return the average to the caller

    

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# ===> Call the subprogram, passing monthlySales to it,
#      and assign the returned value to the correct variable



# ===> Print the average sales to two decimal places using string.format()
#      by completing the pattern inside the { }
# ===> Also add a £ sign at the start of the figure
print("           ".format(averageSales))
