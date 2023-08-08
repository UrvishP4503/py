from string import ascii_letters
alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27,
    'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
    'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
}


def left_split(arr: list[str]):
    ans = []
    for i in arr:
        l = len(i) // 2
        ans.append(set(i[:l]))
    return ans


def right_split(arr: list[str]):
    ans = []
    for i in arr:
        l = len(i) // 2
        ans.append(set(i[l:]))
    return ans


def point_list(left, right) -> list[int]:
    temp_list = []
    ans = []
    for i in range(0, len(left)):
        temp_list.append(left[i].intersection(right[i]))
    for i in temp_list:
        temp = 0
        for j in i:
            temp += alphabet_dict[j]
        ans.append(temp)
    return ans


with open("input03.txt") as file:
    backpack = [i for i in file.read().strip().split("\n")]

left = left_split(backpack)
right = right_split(backpack)

list_of_points = point_list(left, right)

print(sum(list_of_points))


part2 = 0
j = 3
for i in range(0, len(backpack), 3):
    sacks = backpack[i:j]
    j += 3
    for val, char in enumerate(ascii_letters):
        if char in sacks[0] and char in sacks[1] and char in sacks[2]:
            part2 += val + 1

print(part2)
