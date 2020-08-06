myList = ["a", "z", "g", "e", "f"]
target = "g"

i = 0
while i < len(myList):
    if target == myList[i]:
        print(i)
        break
    i += 1

for i, element in enumerate(myList):
    if target == element:
        print(i)
        break
