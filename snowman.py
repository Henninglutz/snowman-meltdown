import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    for guess in secret_word:
        if guess in secret_word:
            #for char in secret_word:
            print(f"_"* len(secret_word))

    """
    Loop Print  "_" for every letter 
    (neue Variable mit den bereits geratenen Buchstaben = neuer String) 
    guess print für neuen String in der richtigen Stelle 
    (if guess in secret word guess ???!index im string? replace index mit guess:
    else: print "_")
    Erst Index() = secret_word.index(guess)
    Variabele updaten = dann replace()

    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()