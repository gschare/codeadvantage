students = ["Akshaya", "Rahstin", "Jasmine", "Avik", "Anish", "Ian"]

other_students = ["Bob", "Yaniv", "Adiba", "Marilyn", "Yaniv"]
other_students[1] = 500

print(type(other_students[1]))

print(other_students)

#new_students = students + other_students

students.extend(other_students)

#print(students)

##index = 0
##while index < len(students):
##    print(students[index])
##    print(index)
##    index += 1

