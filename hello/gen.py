def gen_fun(iter: list):
    for i in iter:
        if i % 2 == 0:
            yield i
        else:
            yield i + 1


if __name__ == "__main__":
    arr = [1, 4, 56, 37, 8, 4, 5, 7, 346, 65]
    for i in gen_fun(arr):
        print(f"{i} ", end="")
