import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown","masterschool"]
mistakes = 0


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    global mistakes
    global momentum
    secret_word = get_random_word()
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")
    print(f"Secret word selected: " + "_" * len(secret_word))
    while True:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess not in secret_word:
            mistakes += 1
            print(ascii_art.STAGES[mistakes - 1])
        else:
            print(f"_" * len(secret_word))

        if guess not in guessed_letters:
            guessed_letters.append(guess)
        momentum = ""
        for char in secret_word:
            if char in guessed_letters:
                momentum += char + " "
            else:
                momentum += "_"
        print(momentum)
        # Game won / lost: if... = break
        if "_" not in momentum:
            print("Kudos! You won!")
            break
        if mistakes >= len(ascii_art.STAGES):
            print("GAME OVER")
            print("*********")
            print("do you want to play again? y/n?")
            restart = input("")
            if restart.lower() == "y":
                mistakes = 0
                play_game()
            break


if __name__ == "__main__":
    play_game()