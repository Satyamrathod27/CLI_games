import random

CHOICES = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

WIN_RULES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def get_user_choice():
    """Prompt user until valid choice is entered."""
    while True:
        user_input = input("Choose Rock, Paper, Scissors (r/p/s): ").strip().lower()

        # allow full words too
        if user_input in ("rock", "paper", "scissors"):
            return user_input
        if user_input in CHOICES:
            return CHOICES[user_input]

        print("❌ Invalid input! Please type r/p/s or rock/paper/scissors.\n")


def get_computer_choice():
    return random.choice(list(CHOICES.values()))


def decide_winner(user, computer):
    """Return 'user', 'computer', or 'tie'."""
    if user == computer:
        return "tie"
    if WIN_RULES[user] == computer:
        return "user"
    return "computer"


def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "tie":
        print("🤝 It's a tie!\n")
    elif result == "user":
        print("🎉 You win this round!\n")
    else:
        print("💻 Computer wins this round!\n")

    return result


def get_best_of():
    """Ask if user wants best-of mode; return target wins."""
    while True:
        mode = input("Play Best-of? (e.g., 3/5/7) or press Enter for normal mode: ").strip()

        if mode == "":
            return None

        if mode.isdigit():
            n = int(mode)
            if n > 0 and n % 2 == 1:
                return (n // 2) + 1
            else:
                print("❌ Best-of must be a positive odd number (3, 5, 7...).\n")
        else:
            print("❌ Please enter a number like 3 or press Enter.\n")


def main():
    print("🎮 Welcome to Rock Paper Scissors (CLI)!\n")

    while True:
        user_score = 0
        computer_score = 0
        ties = 0

        target_wins = get_best_of()

        print("\nGame Started! Type 'r', 'p', 's' or full words.\n")

        while True:
            result = play_round()

            if result == "user":
                user_score += 1
            elif result == "computer":
                computer_score += 1
            else:
                ties += 1

            print(f"📌 Score => You: {user_score} | Computer: {computer_score} | Ties: {ties}\n")

            # Best-of mode
            if target_wins:
                if user_score == target_wins:
                    print("🏆 You won the match!\n")
                    break
                if computer_score == target_wins:
                    print("🏆 Computer won the match!\n")
                    break
            else:
                again = input("Play another round? (y/n): ").strip().lower()
                if again != "y":
                    break

        restart = input("Start a new game? (y/n): ").strip().lower()
        if restart != "y":
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
