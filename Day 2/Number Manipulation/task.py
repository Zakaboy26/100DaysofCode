bmi = 84 / 1.65 ** 2
print (bmi)

#We want to round the bmi (30.85399449035813)
print (round(bmi)) #This outputs 31

#What if we want to 2 decimal places?
print (round(bmi,2)) #This outputs 30.85



score1 = 0
score2 = 0
isWinning = True
#User scores point
score1 = score1 + 1 #This is long when u have to manipulate values a lot in Python
score2 += 1 #This does the same thing (or u add minus) and is a lot quicker
print ("score1 =", score1, "\nscore2 =", score2)

#F Strings makes it easy to mix strings and data types
print("Your score is " + str(score2)) #Long having to convert string every time

#So we do this instead
print(f"Your score is {score1}, your bmi is {bmi} and you are winning = {isWinning}")
