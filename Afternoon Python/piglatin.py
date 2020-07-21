greeting = "hello "
world = "world"

greeting[0:3] # -> "hel"
world[3:] # -> "ld"
greeting + world # -> "hello world"
greeting.split("e") # -> ["h", "llo"]
greeting*3 # -> "hello hello hello "

sentence = input("Write a sentence: ")
# Gregory -> Egorygray
# My name is Gregory -> Ymay Amenay Isay Egorygray
# to -> otay
# if -> ifay

# ant -> antay

vowels = ['a', 'e', 'i', 'o', 'u']

sentence = sentence.split(" ")
print(sentence)
output = []
for word in sentence:
    if word[0].lower() in vowels:
        output.append(word + "ay")
    else:
        index = min([word.find(v) for v in vowels if word.find(v)!=-1])
        output.append(word[index:] + word[:index].lower() + "ay")
print(output)
