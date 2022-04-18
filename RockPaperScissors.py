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
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors "))
print(type(user_choice))
if user_choice == 0:
  print(f"You chose, \n {rock}")
elif user_choice == 1:
  print(f"You chose, \n {paper}")
else:
  print(f"You chose, \n {scissors}")

pc_choice = random.choice(game_images)
print(f"Computer chose, {pc_choice}")

if pc_choice == rock and user_choice == 0:
    print('It\'s a draw')
if pc_choice == paper and user_choice == 1:
    print('It\'s a draw')
if pc_choice == scissors and user_choice == 2:
    print('It\'s a draw')
elif pc_choice == rock and user_choice == 1:
    print('user wins!')
elif pc_choice == rock and user_choice == 2:
    print('Computer Wins!')
elif pc_choice == paper and user_choice == 0:
    print('Computer Wins!')
elif pc_choice == paper and user_choice == 2:
    print('User Wins!')
elif pc_choice == scissors and user_choice == 0:
    print('User Wins')
elif pc_choice == scissors and user_choice == 1:
    print('Computer Wins!')
