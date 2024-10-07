import random

options = ['rock', 
           'paper', 
           'scissors']

computer_choice = random.choice(options)

user_choice = input('do you want rock, paper, or scissors?\n').lower()

if computer_choice == user_choice:
    print(f"computer chose {computer_choice}, It's a TIE!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(f'computer chose {computer_choice}, YOU WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f'computer chose {computer_choice}, YOU WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(f'computer chose {computer_choice}, YOU WIN')
else:
    print(f'computer chose {computer_choice}, YOU LOSE')