'''
Examples of built-in functions:

print("Hello") # write to shell
input() # user writes something, computer stores it
min(8, 7) # smallest of something
import math
math.sqrt(4) # takes the square root of a number
length = len("hello") # count the length of the string or list
range(5)

Now let's write our own functions!
'''

# A function is something that:
# - takes something in
# - does something with it
# - spits something else back out

def f(x):    
    return x + 1

def firstletter(word):
    return word[0]

def firstelement(L):
    return L[0]

# Convert Fahrenheit to Celsius
def F2C(temperature):
    celsius = ((temperature - 32)*5)/9
    return celsius

# Count the words in a sentence
def countwords(sentence):
    words = sentence.split(" ")
    filtered_words = []
    for word in words:
        if word != "":
            filtered_words.append(word)
    return len(filtered_words)

# contains() takes a word and a letter to look for
# and returns true if the letter is in the word.
# false otherwise.
def contains(word, target):
    for letter in word:
        if letter == target:
            return True
    return False

print(contains("world", "r"))

# Homework:
# convert the entire palindrome algorithm to be a single function
# called isPalindrome(word) which takes a word and returns True or False.







    
