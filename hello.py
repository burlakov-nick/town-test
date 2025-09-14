def main():
    print("Hello world!")


def sum_2(a, b):
    return a + b


def mul(a, b):
    return a * b


def sum_3(a, b, c):
    return sum_2(sum_2(a, b), c)


def sum_4(a, b, c, d):
    return sum_2(sum_2(a, b), sum_2(c, d))


INIT = 0


def add(*args):
    r = INIT
    # sum everything
    for arg in args:
        r += arg
    return r


if __name__ == "__main__":
    print(sum_3(1, 2, 3))
    print(sum_3(1, 2, 6))
    print(sum_4(1, 2, 3, 4))
    print(sum_3(1, 2, 6))
    add(1, 2, 3)
    add(1, 2, 3, 4)
    add(1, 2, 3, 4, 5)

    # for future changes
    add2 = lambda x: add(x, 2)
    print(add2(1))

    print("all done")