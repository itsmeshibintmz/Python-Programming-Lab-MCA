startYear=int(input("Enter the start year\n"))
endYear=int(input("Enter the end year\n"))
print("Leap years between",startYear,"and",endYear,"are:")
for year in range(startYear,endYear+1):
    if year%4==0 and year%100!=0 or year%400==0:
        print(year)