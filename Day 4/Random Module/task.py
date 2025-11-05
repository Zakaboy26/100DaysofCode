import random
import my_module


random_num = random.randint(1,10)
print(random_num)
#Output example: random number 1-10
print(my_module.my_favourite_number)
#Output example: own module so 3.1415

#Returns the next random floating point number in the range 0.0 <= X <1 (1 is NOT incl)
random_float = random.random()
print(random_float)
#Output example: 0.7965938860872885, never 1 though


#We can also multiply this though....
random_float_two = random.random() * 10
print(random_float_two)
#Output example: 9.840089553346228

random_float_three = random.uniform(1,10)
print(random_float_three)
#Output: basically same but its possible u get the upperbound (10)


#import random
print("WELCOME TO HEADS OR TAILS NIGGA")
userPick = input("Heads or Tails fuck nigga? H/T: ").lower()
coinFlip = random.randint(1,2)
if coinFlip == 1:
    print("Its Heads!")
    if userPick == "T":
        print("You lose")
    else:
        print ("U won gang")
if coinFlip == 2:
    print("It's Tails!")
    if userPick == "H":
        print("You lose")
    else:
        print("You win nigga I always believed in you")



























