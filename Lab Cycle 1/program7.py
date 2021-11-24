# Program to display leap years b/w two inputted years.

# Prompt user for input
startYear=int(input("Enter the start year\n"))
endYear=int(input("Enter the end year\n"))
#Displaying the leap years
print("Leap years between",startYear,"and",endYear,"are:")
# loop to check whether the year is leap year or not
for year in range(startYear,endYear+1):
    if year%4==0 and year%100!=0 or year%400==0:
        print(year)