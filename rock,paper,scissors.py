
#rock paper scissors

import random
def play():
    print("Welcome!")
    choices = (["rock", "paper", "scissors"])

    user_choice = input("Rock, Paper or scissors? ")
    computer_choice = random.choice(choices)



    if user_choice == computer_choice:
        return "Its a tie!"

    if is_win(user_choice, computer_choice):
        return f"You Win!\nComputers choice was {computer_choice}."
    return f"You Lose!\nComputers choice was {computer_choice}."


def is_win(user, computer):

    if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return True
    return False




if __name__ == "__main__":
    print(play())
