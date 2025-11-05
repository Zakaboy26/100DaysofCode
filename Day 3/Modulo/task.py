#Modulo operator (%) it goes in between 2 numbers and it works out what is the
# remainder after division

# so 10 % 5 ('10 modulo 5') would give 0 as it divides 'cleanly'
# 10 % 3 would be 1 because its not dividing 'cleanly' (10/3 = 3 w 1 remaining)
# BASICALLY 3 FITS INTO 10 3 WHOLE TIMES (TILL 9) REMAINDER IS 1
# SO 6 % 4 = 2 , SINCE 4 ONLY FITS ONCE INTO 6, SO THERE'S 2 REMAINING

#Check odd or even
Usernumber = int(input("Please enter a number to see if its odd or even: "))

if Usernumber % 2 == 0:
    print(f"Your number >>> {Usernumber} \nis even!")
else:
    print(f"Look at dis uneven ahh number >>> {Usernumber} \nweak ahh")

username = input("Enter your name to see if it has odd or even numbers")
length_of_username = len(username)
if length_of_username % 2 == 0:
    print("Your name has even numbers!")
else:
    print(f"Your name {username} has uneven numbers bruh")