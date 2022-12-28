from random import shuffle


def IsTrue(box, guess):
    if box[guess - 1] == "O":
        print("Your guess is correct")
        print(box)
    else:
        print("Your guess was wrong")
        print(box)


def Guess():
    box = ["", "O", ""]
    shuffle(box)
    guess = ""
    while guess not in ["1", "2", "3"]:
        guess = input("Enter a number: ")
    IsTrue(box, int(guess))


Guess()
