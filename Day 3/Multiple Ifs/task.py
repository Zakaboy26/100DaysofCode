print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
totalBill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    pictureTaken = input("Do you want a picture taken? Y/N")
    if pictureTaken == "Y":
        totalBill +=  3
    if age <= 12:
        totalBill += 5
    elif age <= 18:
        totalBill += 7
    else:
        totalBill += 12
    print(f"Please pay £{totalBill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
