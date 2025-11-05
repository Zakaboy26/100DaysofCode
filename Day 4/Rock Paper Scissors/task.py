rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#MY SOLUTION, WORKS BUT LOTS OF BOILERPLATE CODE
"""import random
userHand = input("Let's play rock paper and scissors! Press 1 for rock, 2 for paper and 3 for scissors:\n")
hands = [rock, paper, scissors]
roboPick = random.choice(hands)

if userHand == "1":
    print("You picked: \n", hands[0])
    if roboPick == (hands[0]):
        print("Robot picked: \n", roboPick)
        print("Draw")
    elif roboPick == (hands[1]):
        print("Robot picked: \n", roboPick)
        print("You lose")
    else:
        print("Robot picked: \n", roboPick)
        print("You win")

if userHand == "2":
    print("You picked: \n", hands[1])
    if roboPick == (hands[0]):
        print("Robot picked: \n", roboPick)
        print("You win")
    elif roboPick == (hands[1]):
        print("Robot picked: \n", roboPick)
        print("Draw")
    else:
        print("Robot picked: \n", roboPick)
        print("You lose")

if userHand == "3":
    print("You picked: \n", hands[2])
    if roboPick == (hands[0]):
        print("Robot picked: \n", roboPick)
        print("You lose")
    elif roboPick == (hands[1]):
        print("Robot picked: \n", roboPick)
        print("You win")
    else:
        print("Robot picked: \n", roboPick)
        print("Draw")
else:
    print("Invalid number")"""

#ANGELA YU SOLUTION
import random
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

