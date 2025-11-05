#Using for loops with the range function:
#for number in range(1,10):
#    print(number) #This prints till 9, if u want 1-10 u need to set the range to 11

#If you want to increase by any other number you specify how large u want the step to be
#for number in range(1,11,3): #this prints in increments of 3
#    print(number)

#How can you add all numbers from 1-100 using this? exercise
sum = 0
for number in range (1,101):
    sum += number
print(sum)

#exercise: fizzbuzz my own solution
for number in range (1,101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)