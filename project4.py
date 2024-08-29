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
import random
game_image=[rock,paper,scissors]
user_choice=int(input("what do you choose . typer 0 for rock ,1 for paper and 2 for scissor\n"))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print(f"the computer choose:{computer_choice}")
print(game_image[computer_choice])

if user_choice >=3  and computer_choice<0:
    print("you entered invalid number")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==2 and computer_choice==0:
    print("I win")
elif computer_choice>user_choice:
    print("I win")
elif computer_choice>user_choice:
    print("you win")
elif computer_choice == user_choice:
    print("it's draw")