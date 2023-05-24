def do_stuff(para: int) -> int:
    try:
        return int(para) * 69
    except ValueError as err:
        return err


def do_more_stuff(para1, para2):
    return para1 * para2
