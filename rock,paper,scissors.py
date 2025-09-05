# Rock beats scissors, scissors beats paper, paper beats rock

import random


def play(user_score, computer_score):
    print("Welcome to Rock Paper Scissors!")


    choices = ["rock", "paper", "scissors"]


    user = input("Please choose: rock, paper, scissors? ").lower().strip()
    while user not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user = input("Please choose: rock, paper, scissors? ").lower().strip()


    computer = random.choice(choices)


    print(f"Computer Choice: {computer}")


    if user == computer:
        computer_score += 1
        user_score += 1
        return f"It's a draw! Score: You {user_score} - Computer {computer_score}", user_score, computer_score


    if is_Win(user, computer):
        user_score += 1
        return f"You Won! Score: You {user_score} - Computer {computer_score}", user_score, computer_score


    computer_score += 1
    return f"You Lose! Score: You {user_score} - Computer {computer_score}", user_score, computer_score


def is_Win(user, computer):
    if (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') \
            or (user == 'paper' and computer == 'rock'):
        return True
    return False


if __name__ == "__main__":
    user_score = 0
    computer_score = 0


    result, user_score, computer_score = play(user_score, computer_score)
    print(result)


    again = input("Would you like to play again? (y/n) ").lower().strip()
    while again == "y":
        result, user_score, computer_score = play(user_score, computer_score)
        print(result)
        again = input("Would you like to play again? (y/n) ").lower().strip()

    print(f"Final Score: You {user_score} - Computer {computer_score}")
    print("Thanks for playing!")
