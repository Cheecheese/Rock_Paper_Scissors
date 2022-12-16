import random

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

game = [rock, paper, scissors]
user = int(input("Choose one of the three options. Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >= 3 or user < 0:
    print("You type an invalid number, you lose!.")
else:
    print(game[user])
    com = random.randint(0, 2)
    print("Computer chose:")
    print(game[com])

    if user == 0 and com == 2:
        print("You win!")
    elif com == 0 and user == 2:
        print("You lose.")
    elif com > user:
        print("You lose.")
    elif user > com:
        print("You win!")
    elif com == user:
        print("It's a draw, try again.")
