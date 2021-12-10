# Getting input from user
text=input("Enter a text: ")
print("The text is: ",text)
print("Word count is: ")
# Function to count the number of words in the text
def word_count(str):
    # Splitting the text into words
    counts = dict()
    words = str.split()

    # Looping through the words
    for word in words:
        # Checking if the word is already in the dictionary
        if word in counts:
            # Incrementing the count of the word
            counts[word] += 1
        else:
            # Adding the word to the dictionary
            counts[word] = 1
    # Returning the dictionary
    return counts

# Calling the function
print(word_count(text))