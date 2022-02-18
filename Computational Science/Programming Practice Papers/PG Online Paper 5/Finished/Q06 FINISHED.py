# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
data = []
num_results = int(0)

phoneNumbers = open("phonenumbers.csv", "r") #file ID
for line in phoneNumbers:
    line = line.strip()# Remove the "/n" from each line

    entries = line.split(",") # Split each line from the file by commas

    data.append(entries)# Add the data to a 2d array


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

query = input("Enter a search term >    ").capitalize() # Make 1st letter upper case

for person in data:
    if person[1] == query: # if Last Name == search term
        print(f"""
        First Name: {person[0]}
        Last Name: {person[1]}
        Phone Number: {person[2]}
        """)# triple quotes allow for blank lines in 1 print statement
        num_results = num_results + 1


print(f"{len(data)} records searched, {num_results} matches found.")