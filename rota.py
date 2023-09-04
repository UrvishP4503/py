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


def is_valid(
        morning: Morning, afternoon: Afternoon, night: Night,
        data: list[int]
) -> tuple[bool, bool, bool]:

    mor = True
    aft = True
    nig = True

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
                afternoon.e += 1
            case post.B.value:
                morning = 1
            case post.BL.value:
                morning.b = 1
            case post.L.value:
                afternoon.l += 1
            case post.N.value:
                night.n += 1
            case _:
                print("not valid input")

    return mor, aft, nig
