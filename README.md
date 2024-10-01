# My Hangman project
## How to play my Hangman game
1. Run the code in terminal by writing python3 hangman.py
2. Input field will ask for a letter, provide a guess of letter
3. When ever you guess the wrong word/letter, you will be presented with a body part. If you guess the correct word/letter, you'll continue
4. If you've guessed all incorrect and lose, we display the Hangman, the correct answer and a lose-str
5. If you guessed the correct word and win, we display the parts of Hangman (incorrect guesses), the correct answer and a win-str

## The Hangman drawing
hangman_drawing = {{0: ("  ",
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
                       " / \\ ")}}

## Words used, provided by prompt in ChatGPT
prompt = provide a set list with commonly used words, of things like "Car", in everyday english language
words provided = ('car', 'house', 'phone', 'book', 'chair', 'table', 'pen', 'computer', 'television')


