# detect whether a word is a palindrome
# e.g. racecar, hannah, bob, dad, mom, eye

def isPalindrome(word):

    # as a for loop. The "-1" argument tells range to step backwards.
    reversed_text = ""
    for i in range(len(word)-1, -1, -1):
        reversed_text = reversed_text + word[i]

    # check if text is the same backwards as well as forwards.
    if (word == reversed_text):
        print(word + " is a palindrome!")
        return True
    else:
        print(word + " is not a palindrome")
        return False

'''
For homework:

Implement the same algorithm, but instead of reversing the entire text,
only reverse the first half of the letters and compare that to the
second half of the letters.
So given "horror", take the first half ("hor") and reverse it to get "roh".
Then compare "roh" == "ror" (the second half). This is false because horror
is not a palindrome.

See if you can figure out how to handle the case where your text has an odd
number of letters, like "racecar". How do you handle having uneven halves?

Why might we do this, you may ask? Because it's twice as fast to only do the
first half of the letters! Programmers care a lot about efficiency.

This is a pretty difficult assignment, so try your best and check your spelling!
'''

'''
If you're super ambitious, you can try writing a program that detects
whether a word has just one extra letter so that without that letter it would
be a palindrome, like "yummy" (remove the "u").
Hint: iteratively splice the list around index i and check if any of those
is a palindrome using the existing code.
'''
