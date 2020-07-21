#inventory = [["banana", 2.99], ["orange", 1.99], ["kiwi", 1.99], ["apple", .99]]
#prices = [2.99, 1.99, 1.99, .99, 3.99, 5.99]

inventory = {
    "banana" : 2.99,
    "orange" : 1.99,
    "kiwi" : 1.99,
    "apple" : .99
    }

inventory["grapefruit"] = 6.99

amount = input("Enter the amount the customer pays: ")    # e.g. '13.75'
item = input("Enter the name of the item: ").lower()   # e.g. 'banana'
amount_of_item = float(input("How many of that item do you want to buy: ")) # integer

'''
i = 0
while i < len(inventory):
    if item == inventory[i]:
        price = prices[i]
        break
    i += 1
'''
'''
i = 0
while i < len(inventory):
    if item == inventory[i][0]:
        price = inventory[i][1]
        break
    i += 1
'''

price = inventory[item]

amount = float(amount)

amount -= price*amount_of_item

if amount < 0:
    print("Customer didn't pay enough!")
    print("Customer needs to pay $" + str(round(-amount)))

else:
    amount *= 100

    dollars = int(amount / 100)
    amount %= 100

    quarters = int(amount / 25)
    amount %= 25

    dimes = int(amount / 10)
    amount %= 10

    nickels = int(amount / 5)
    amount %= 5

    pennies = int(amount)

    print(str(dollars) + " dollars, ")
    print(str(quarters) + " quarters, ")
    print(str(dimes) + " dimes, ")
    print(str(nickels) + " nickels, ")
    print("and " + str(pennies) + " pennies.")
