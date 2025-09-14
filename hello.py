def main():
    print("Hello world!")


def sum_2(a, b):
    return a + b


def mul(a, b):
    return a * b


def sum_3(a, b, c):
    return sum(sum(a, b), c)


def sum_4(a, b, c, d):
    return sum(sum(a, b), sum(c, d))


if __name__ == "__main__":
    main()
