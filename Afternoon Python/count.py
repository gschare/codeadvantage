myList = ["a", "g", "z", "g", "e", "f", "g"]
target = "g"

total = 0
i = 0
while i < len(myList):
    if target == myList[i]:
        total += 1
    i += 1
print(total)

total = 0
for element in myList:
    if target == element:
        total += 1
print(total)
