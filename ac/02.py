points = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

points_final = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

outcome1 = 0
final_outcome = 0
with open("input02.txt") as file:
    rounds = [i for i in file.read().strip().split('\n')]
    for i in rounds:
        outcome1 += points[i]
    for i in rounds:
        final_outcome += points_final[i]

print(outcome1," ")
print(final_outcome," ")
