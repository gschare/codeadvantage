text = input("Enter a word: ")

first_half = ""
for i in range(len(text)//2-1, -1, -1):
    first_half = first_half + text[i]

# is my word an even number of letters
if len(text) % 2 == 0:
    second_half = text[len(text)//2:]
else:
    second_half = text[len(text)//2 + 1:]

if (first_half == second_half):
    print(text + " is a palindrome!")
else:
    print(text + " is not a palindrome")
