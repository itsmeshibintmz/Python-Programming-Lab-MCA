# Program to Get a string from an input string where all occurrences of the first 
# character are replaced with ‘$’, except the first character. [eg: onion -> oni$n]

# Function to replace the occurence of a character with $
def replace_char(str):
    unique_char = set() # To store unique characters
    for i in range(0,len(str)): # loop to get the unique character
        if str[i] in unique_char:
            str=str[:i]+"$"+str[i+1:] # replace the character with $
        else:
            unique_char.add(str[i])  # add the unique character to the set 
    return str

str = input("Enter a string: ")
print(replace_char(str)) # Call the function