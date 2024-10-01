# airdrop mapp från privat dator och använd här
# my hangman-prject for 2 october

import random 

# more words in a set could be placed in a separate file, then imported (from x import words)
words = ('car', 'house', 'phone', 'book', 'chair', 'table', 'pen', 'computer', 'television',
 'window', 'door', 'bag', 'shoe', 'shirt', 'bed', 'lamp', 'bottle', 'glass', 'cup', 
 'spoon', 'fork', 'knife', 'plate', 'bicycle', 'watch', 'camera', 'sofa', 'clock', 
 'keyboard', 'mouse', 'pillow', 'mirror', 'wallet', 'hat', 'jacket', 'bus', 'train', 
 'pencil', 'notebook', 'fridge', 'oven', 'stove', 'backpack', 'fan', 'sink', 
 'toothbrush', 'towel', 'umbrella', 'piano', 'guitar', 'radio')

#dict of key:(tuple)
hangman_drawing = {0: ("  ",
                       "  ",
                       "  "),
                   1: (" o ",
                       "  ",
                       "  "),
                   2: (" o ",
                       " | ",
                       "  "),
                   3: (" o ",
                       "/| ",
                       "   "),
                   4: (" o ",
                       " /|\\ ",
                       "  "),
                   5: (" o ",
                       " /|\\",
                       " / "),
                   6: (" o ",
                       " /|\\",
                       " / \\ ")}

def display_hangman(wrong_guesses): # display body part when guessing wrong word or letter
    for line in hangman_drawing[wrong_guesses]:
        print(line)

def display_hint(hint): #displays a hint whenever we guess the correct letter (str)
    print(" ".join(hint))

def display_answer(answer): # displays the correct answer if guessed
    print(" ".join(answer))

def main(): # contains the main body of our code
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0 # for test purpose, change to a number from 1-6, then run
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue

        guessed_letters.add(guess) 

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(f"The correct answer is: {answer}")
            print("Congratz, you won!")
            is_running = False
        elif wrong_guesses >= len(hangman_drawing) - 1:
            display_hangman(wrong_guesses)
            display_answer(f"The correct answer is: {answer}")
            print("Sorry, you lose")
            is_running = False


if __name__ == "__main__":
    main()