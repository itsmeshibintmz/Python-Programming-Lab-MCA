# Program to perform List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) Form a list ordinal value of each element of a word (Hint: use ord() to get ordinal values)

def positive_list(list):
    return [i for i in list if i>0]

def square_list(list):
    return [i**2 for i in list]

def vowel_list(word):
    return [i for i in word if i in "aeiouAEIOU"]

def ordinal_list(word):
    return [ord(i) for i in word]

print("Enter a list of numbers to generate positive list: ")
list = [int(i) for i in input().split()]
print("Positive list: ", positive_list(list))