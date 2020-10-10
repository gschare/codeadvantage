myList = list(range(50))

newList = []
for number in myList:
    if number > 25:
        newList.append(number)
print(newList)

newList = [x for x in myList if x > 25]
print(newList)

def greaterThan25(x):
    return x > 25

newList = list(filter(greaterThan25, myList))
print(newList)

newList = list(filter(lambda x: x > 25, myList))
print(newList)

######################################################

myList = list(range(11))
newList = []
for number in myList:
    newList.append(number ** 2)
print(newList)

newList = [x**2 for x in myList]
print(newList)

def square(x):
    return x * x

newList = list(map(square, myList))
print(newList)

newList = list(map(lambda x: x*x, myList))

#########################################################

def modifyMessage(func, message):
    return func(message)

def superModifyMessage(func, message):
    return func(func(func(message)))

def exclaim(message):
    return message + "!"

def question(message):
    return message + "?"

def swedish(message):
    output = []
    for c in message:
        output.append(c)
        output.append("f")
    return "".join(output)

print(modifyMessage(question, "Hello World"))
print(superModifyMessage(exclaim, "Hello World"))
print(superModifyMessage(swedish, "Hello World"))