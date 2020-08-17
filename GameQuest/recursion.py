def printn(msg, n):
    for i in range(n):
        print(msg)

# Recursion: a function calling itself inside its definition

def printnRecur(msg, n):
    if n==0:
        return
    print(msg)
    printnRecur(msg, n-1)

# len(iter)
def lengthIter(myList):
    length = 0
    for i in range(myList):
        length += 1
    return length

# iter: a list
def length(myList):
    print(myList)
    if myList==[]:
        return 0
    else:
        return 1 + length(myList[1:])

# factorial:
# 5!
# = 5 * 4 * 3 * 2 * 1
# 3!
# = 3 * 2 * 1
# 1, 2, 3, 4, 5, 6, ...
# 1, 2, 6, 24, 120, 720, ...
def factorial(n):
    # base case
    if n == 0:
        return 1
    # recursive step
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    [print(factorial(x)) for x in range(100)]