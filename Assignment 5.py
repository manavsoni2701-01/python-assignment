# Task 1
students={'alice':85,'ram':95,'manav':75}
name=input("Enter the student's name:")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("student not found")

students={'alice':85,'ram':95,'manav':75}
name=input("enter the student's name:")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("student not found")

#task 2

numbers= list(range(1,11))

first_five=numbers[:5]
reversed_list= first_five[:-1]

print('original list:', numbers)
print('extracted first five elements:', first_five)
print('reversed_list:', reversed_list)
