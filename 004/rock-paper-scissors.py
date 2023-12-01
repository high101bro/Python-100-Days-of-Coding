#! /usr/bin/env python3

import random

print(f"Let's play rock-paper-scissors!")

score_dict = {
    "player": 0,
    "Computer": 0,
    "tie": 0
}

def rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def scissors():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

while True:
    your_choice = input(f"Select rock (r), paper (p), scissors (s), and quit (q): ")
    computer_choice = random.randint(1,3)
    if your_choice == 'r' and computer_choice == 1:
        print(f"Player\n{rock()}")
        print(f"Computer\n{rock()}")
        print("You tied.")
        score_dict["tie"] += 1
    elif your_choice == 'r' and computer_choice == 2:
        print(f"Player\n{rock()}")
        print(f"Computer\n{paper()}")
        print("You lost.")
        score_dict["Computer"] += 1
    elif your_choice == 'r' and computer_choice == 3:
        print(f"Player\n{rock()}")
        print(f"Computer\n{scissors()}")
        print("You won.")
        score_dict["player"] += 1

    elif your_choice == 'p' and computer_choice == 1:
        print(f"Player\n{paper()}")
        print(f"Computer\n{rock()}")
        print("You won.")
        score_dict["player"] += 1
    elif your_choice == 'p' and computer_choice == 2:
        print(f"Player\n{paper()}")
        print(f"Computer\n{paper()}")
        print("You tied.")
        score_dict["tie"] += 1
    elif your_choice == 'p' and computer_choice == 3:
        print(f"Player\n{paper()}")
        print(f"Computer\n{scissors()}")
        print("You lost.")
        score_dict["Computer"] += 1

    elif your_choice == 's' and computer_choice == 1:
        print(f"Player\n{scissors()}")
        print(f"Computer\n{rock()}")
        print("You lost.")
        score_dict["Computer"] += 1
    elif your_choice == 's' and computer_choice == 2:
        print(f"Player\n{scissors()}")
        print(f"Computer\n{paper()}")
        print("You won.")
        score_dict["player"] += 1
    elif your_choice == 's' and computer_choice == 3:
        print(f"Player\n{scissors()}")
        print(f"Computer\n{scissors()}")
        print("You tied.")
        score_dict["tie"] += 1
    elif your_choice == 'q':
        if score_dict["player"] > score_dict["Computer"]:
            print("Congratuations. You won overall!")
        if score_dict["player"] < score_dict["Computer"]:
            print("Better luck next time... You lost overall!")
        if score_dict["player"] == score_dict["Computer"]:
            print("Will you look at that? You tied overall!")
        quit()
    else:
        print("You can't make that selection.")

    player_score = score_dict["player"]
    Computer_score = score_dict["Computer"]
    tie_score = score_dict["tie"]
    print(f"The score is: Player {player_score} - Computer {Computer_score} - Tie {tie_score}")
    print('')
