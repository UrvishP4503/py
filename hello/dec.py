def my_decorator(arg_func):
    def wrapr_func(*args, **kwargs):
        print(f"-------------")
        arg_func(*args, **kwargs)
        print(f"-------------")
    return wrapr_func


@my_decorator
def foo(name, age=0):
    print(f"hi {name} i see you are {age} year old")


if __name__ == "__main__":
    foo("baba", 1000)
    foo("Urvish", 19)
