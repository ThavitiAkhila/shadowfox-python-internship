import random


words = {
    "python": {
        "hint": "A popular programming language",
        "category": "Programming"
    },
    "computer": {
        "hint": "An electronic machine used to process data",
        "category": "Technology"
    },
    "internet": {
        "hint": "A worldwide network of computers",
        "category": "Technology"
    },
    "elephant": {
        "hint": "The largest land animal",
        "category": "Animals"
    },
    "football": {
        "hint": "A popular team sport",
        "category": "Sports"
    },
    "rainbow": {
        "hint": "A colorful arc seen after rain",
        "category": "Nature"
    }
}


hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def choose_word():
    return random.choice(list(words.keys()))


def display_word(word, guessed_letters):

    result = ""

    for letter in word:

        if letter in guessed_letters:
            result += letter + " "

        else:
            result += "_ "

    return result.strip()


def play_game():

    word = choose_word()

    hint = words[word]["hint"]
    category = words[word]["category"]

    guessed_letters = set()

    wrong_guesses = 0

    max_wrong_guesses = 6

    print()
    print("==============================")
    print("        HANGMAN GAME")
    print("==============================")

    print("Category:", category)
    print("Hint:", hint)

    while wrong_guesses < max_wrong_guesses:

        print(hangman_stages[wrong_guesses])

        print(
            "Word:",
            display_word(word, guessed_letters)
        )

        print(
            "Wrong guesses:",
            wrong_guesses,
            "/",
            max_wrong_guesses
        )

        if guessed_letters:
            print(
                "Guessed letters:",
                " ".join(sorted(guessed_letters))
            )

        guess = input(
            "\nEnter a letter or type 'hint': "
        ).lower().strip()

        if guess == "hint":

            print("Hint:", hint)

            continue

        if len(guess) != 1 or not guess.isalpha():

            print(
                "Please enter exactly one letter."
            )

            continue

        if guess in guessed_letters:

            print(
                "You already guessed that letter."
            )

            continue

        guessed_letters.add(guess)

        if guess in word:

            print("Correct guess!")

        else:

            wrong_guesses += 1

            print("Wrong guess!")

        if all(
            letter in guessed_letters
            for letter in word
        ):

            print(hangman_stages[wrong_guesses])

            print(
                "Congratulations!"
            )

            print(
                "You guessed:",
                word
            )

            return

    print(hangman_stages[wrong_guesses])

    print()
    print("Game over!")

    print(
        "The correct word was:",
        word
    )


def main():

    while True:

        play_game()

        again = input(
            "\nPlay again? (yes/no): "
        ).lower().strip()

        if again not in ["yes", "y"]:

            print(
                "Thanks for playing!"
            )

            break


if __name__ == "__main__":
    main()