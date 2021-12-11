# Program to accept a list of words and return the length of the longest word.

def longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
            longest_word = word
    print("Longest word is",longest_word)
    print("Length of longest word is",longest)

print("Enter a list of words separated by spaces: ")
words = input().split()
longest_word(words)
