list_of_nums = []
number_of_items = int(input("How many numbers do you want to add? "))
'''
i = 0
while i < number_of_items:
    num = input("Enter a number: ")
    num = int(num)
    list_of_nums.append(num)
    i += 1
'''

# [0, 1, 2, 3]
for x in range(number_of_items):
    num = int(input("Enter a number: "))
    list_of_nums.append(num)

'''
total = 0
i = 0
while i < len(list_of_nums):
    total += list_of_nums[i]
    i += 1
'''

total = 0
for x in list_of_nums:
    total += x

print(total)
