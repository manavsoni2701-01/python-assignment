#task 1: Check if number is even or odd

num= int(input('enter a number:'))

if num % 2 ==0:
    print('even')
else:
    print('odd')

numb=int(input('enter a number:'))
if numb % 2 ==0:
    print('even')
else:
    print('odd')

#task 2:Sum of integers from 1 to 50 using  a loop

total=0
for i in range(1,51):
    total=total+i
    print(f"The sum of numbers from 1 to 50 is: {total}")
