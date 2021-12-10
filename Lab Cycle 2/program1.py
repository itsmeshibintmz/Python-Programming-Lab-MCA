# Getting input from user
text=input("Enter a text: ")
print("The text is: ",text)
print("Word count is: ")
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(text))