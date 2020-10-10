'''
Basic string operations:

greeting = "hello "
world = "world"

greeting[0:3]       # -> "hel"
world[3:]           # -> "ld"
greeting + world    # -> "hello world"
greeting.split("e") # -> ["h", "llo"]
greeting*3          # -> "hello hello hello "
'''

# Convert a sentence to pig latin by the following pattern:
# hello -> ellohay
# am -> amay
# great -> eatgray

sentence = input("Write a sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']

sentence = sentence.split(" ")

output = []
for word in sentence:
    if word[0].lower() in vowels:
        output.append(word + "ay")
    else:
        vowel_places = [word.find(v) for v in vowels if word.find(v)!=-1]
        if vowel_places:   # "if vowel_places has stuff in it"
            index = min(vowel_places)
        else:
            index = 1
        '''
        A faster way of doing the above:
        index = min(vowel_places) if vowel_places else 1
        '''
        output.append(word[index:] + word[:index].lower() + "ay")
        
print(" ".join(output))
