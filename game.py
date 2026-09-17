print("Welcome to the Rock,Paper,Scissors game:")
help=input("press enter to start....or type (Help) for the rules\n").capitalize()
if help == "Help":
    print("""
    *******RULES*****
    11) You choose and the computer chooses
    2) Rock smashes Scissors -> Rock wins
    3) Scissors cut Paper -> Scissors win
    4) Paper covers Rock -> Paper wins
    """)
import random
choices=["rock","paper","scissors"]
computer_choice=random.choice(choices)
your_choice=input("enter your choise:\n").lower()
if computer_choice =="rock":
    print(f"the computer choice is {computer_choice}\n")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice=="scissors":
    print(f"the computer choice {computer_choice}\n")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""") 
elif computer_choice=="paper":
    print(f"the computer choise {computer_choice}\n")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")    
if your_choice=="paper":
    print(f"your choise {your_choice}\n")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")        
elif your_choice=="rock":
    print(f"your choice {your_choice}\n")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif your_choice=="scissors":
    print(f"your choise {your_choice}\n")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("invalid choise")
if your_choice==computer_choice:
    print("It is tie!")
elif your_choice=="rock"and computer_choice=="paper"or your_choice=="scissors"and computer_choice=="rock"or your_choice=="paper"and computer_choice=="scissors":
    print("you lost")
else:
    print("congratulations, you win🥳🥳")               
    
