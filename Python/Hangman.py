from utils.hangman_utils import draw_man

answer = "Hello, world!"
letters_guessed = []


def get_strikes():
    return len(list(filter(lambda c: c.isalpha() and c not in answer.lower(), letters_guessed)))


def print_answer_progress():
    print(''.join([c if c.lower() in letters_guessed or not c.isalpha() else '_' for c in answer]))


while get_strikes() < 6 and any([c.isalpha() and c not in letters_guessed for c in answer.lower()]):
    draw_man(get_strikes())
    print_answer_progress()
    print('Letters guessed: [' + ', '.join(letters_guessed) + ']')
    next_guess = input('Guess another letter: ')
    if len(next_guess) == 1 and next_guess.lower() not in letters_guessed:
        letters_guessed.append(next_guess.lower())


if get_strikes() < 5:
    print("Congratulations! You won!")
else:
    print("You lost! The answer is " + answer)
