def compute(data):
    """
    >>> compute("389125467")
    '67384529'
    """
    cups = [*map(int, data)]
    n = len(cups)

    for i in range(100):
        i %= n
        selected = cups[0]
        picked_up = cups[1:4]
        destination_index = cups.index(
            next(
                dest_val
                for delta in range(1, 5)
                if (dest_val := ((selected - delta - 1) % n) + 1) not in picked_up
            )
        )
        cups = (
            cups[4 : destination_index + 1] + picked_up + cups[destination_index + 1 :] + cups[0:1]
        )

    one_index = cups.index(1)
    return "".join(map(str, cups[one_index + 1 :] + cups[:one_index]))


def main():
    print(compute("496138527"))


if __name__ == "__main__":
    main()
