# Program to display leap years between two inputted years.

# Getting starting and ending years from the user
startYear=int(input("Enter the start year\n"))
endYear=int(input("Enter the end year\n"))

print("Leap years between",startYear,"and",endYear,"are:")

# Looping through the years and checking if they are leap years
for year in range(startYear,endYear+1):
    if year%4==0 and year%100!=0 or year%400==0:
        # if yes, print the year
        print(year)

""""
Algorithm
---------
Step 1: Get the starting and ending years from the user
Step 2: Loop through the years and check if they are leap years until the end year
            if year%4==0 and year%100!=0 or year%400==0:
                goto Step 3
Step 3: Print the year
Step 4: End
"""