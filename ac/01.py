with open("input01.txt") as file:
    ans = []
    temp = 0
    for i in file:
        if i != "\n":
            temp += int(i[:i.find("\n")])
        else:
            ans.append(temp)
            temp = 0

top_three = sorted(ans, reverse=True)[:3]
print(max(ans))
print(sum(top_three))
