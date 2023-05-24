import random


def run_guess(guess, answer) -> bool:
    if 0 < int(guess) < 11 and answer == guess:
        print('you are a genius!')
        return True
    else:
        print(f"its not {guess}")
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
