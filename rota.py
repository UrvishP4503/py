from enum import Enum


class Morning:
    def __init__(self) -> None:
        self.s = 0
        self.e = 0
        self.b = 0
        self.ef = 0


class Afternoon:
    def __init__(self) -> None:
        self.s = 0
        self.l = 0
        self.lf = 0


class Night:
    def __init__(self) -> None:
        self.ns = 0
        self.n = 0


class post(Enum):
    ES = 0
    ESLS = 1
    LS = 2
    NS = 3
    EF = 4
    LF = 5
    E = 6
    EL = 7
    B = 8
    BL = 9
    L = 10
    N = 11


def is_valid_data(morning: Morning, afternoon: Afternoon, night: Night, data: list[int]):
    for i in data:
        match i:
            case post.ES.value:
                morning.s = 1
            case post.ESLS.value:
                morning.s = 1
                afternoon.s = 1
            case post.LS.value:
                afternoon.s = 1
            case post.NS.value:
                night.ns = 1
            case post.EF.value:
                morning.ef = 1
            case post.LF.value:
                afternoon.lf = 1
            case post.E.value:
                morning.e += 1
            case post.EL.value:
                morning.e += 1
                afternoon.l += 1
            case post.B.value:
                morning.b = 1
            case post.BL.value:
                morning.b = 1
            case post.L.value:
                afternoon.l += 1
            case post.N.value:
                night.n += 1
            case _:
                print("not valid input")


def is_valid_shift(morning: Morning, afternoon: Afternoon, night: Night) -> tuple[bool, bool, bool]:
    morning_shift = False
    afternoon_shift = False
    night_shift = False
    if (morning.s == 1) and (morning.ef == 1) and (morning.e == 3) and (morning.b == 1):
        morning_shift = True
    if (afternoon.s == 1) and (afternoon.lf == 1) and (afternoon.l == 3):
        afternoon_shift = True
    if (night.ns == 1) and (night.n == 1):
        night_shift = True

    return morning_shift, afternoon_shift, night_shift


test_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]

m = Morning()
a = Afternoon()
n = Night()

print(m.e)
