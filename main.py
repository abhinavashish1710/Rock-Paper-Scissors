import random

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0
draws = 0

print("=" * 35)
print("   ROCK PAPER SCISSORS GAME")
print("=" * 35)

while True:
    player = input("\nChoose Rock, Paper or Scissors: ").capitalize()

    computer = random.choice(choices)

    print("\nYou chose     :", player)
    print("Computer chose:", computer)

    if player == computer:
        print("\n🤝 It's a Draw!")
        draws += 1

    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        print("\n🎉 You Win!")
        player_score += 1

    elif player in choices:
        print("\n💻 Computer Wins!")
        computer_score += 1

    else:
        print("\n❌ Invalid Choice!")
        continue

    print("\n------ SCOREBOARD ------")
    print("You      :", player_score)
    print("Computer :", computer_score)
    print("Draws    :", draws)

    play_again = input("\nPlay Again? (Y/N): ").upper()

    if play_again != "Y":
        break

print("\nThanks for playing!")