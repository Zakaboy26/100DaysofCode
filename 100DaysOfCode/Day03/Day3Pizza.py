print("Welcome to Python Pizza Deliveries!")
finalBill = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    finalBill += 15
if size == "M":
    finalBill += 20
if size == "L":
    finalBill += 25
if extra_cheese == "Y":
    finalBill += 1
if pepperoni == "Y":
    if size == "S":
        finalBill += 2
    else:
        finalBill += 3
print(f"Your final bill is: ${finalBill}.")

