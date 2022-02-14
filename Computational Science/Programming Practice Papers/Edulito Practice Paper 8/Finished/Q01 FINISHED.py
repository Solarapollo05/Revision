#Edulito practice exams 2 1CP2/02 Q01

# ----- Global -----
product = ''
size = ''
n = 1
product_code = ''

# ----- Main -----
product = input("Enter the name of the product.")
size = input("Enter the size of the product.")

n = str(n)

product_code = product[0:2] + size + n

print("The product code is", product_code)



