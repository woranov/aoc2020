class Cup:
    value: int
    next: "Cup"

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def skip(self, n):
        cup = self
        for _ in range(n):
            cup = cup.next
        return cup

    def insert(self, cups):
        curr_next = self.next
        self.next = cups[0]
        cups[-1].next = curr_next

    def __iter__(self):
        cup = self
        yield cup
        while cup := cup.next:
            yield cup

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.skip(item)
        elif isinstance(item, slice):
            cups = [self.skip(item.start)]

            for _ in range(item.stop - item.start - 1):
                cups.append(cups[-1].next)

            return cups
        else:
            raise TypeError(item)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Cup):
            return (self.value, self.next) == (other.value, other.next)
        elif isinstance(other, int):
            return int(self) == other
        else:
            return False

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        next_repr = " (last)" if self.next is None else ""
        return f"<{type(self).__name__} {self.value!r}{next_repr}>"


def compute(data):
    """
    >>> compute("389125467")
    149245887792
    """
    maximum = 1_000_000
    moves = 10_000_000
    # maximum = 9
    # moves = 100

    cup_ns = [*map(int, data), *range(10, maximum + 1)]

    by_value = {}

    curr = first = Cup(cup_ns[0], None)
    by_value[first.value] = first

    for cup_n in cup_ns[1:]:
        new = curr.next = Cup(cup_n, None)
        by_value[new.value] = new
        curr = new

    curr.next = first
    cup = first

    for i in range(moves):
        picked_up = cup[1:4]

        values = ((int(cup) - delta - 1) % maximum + 1 for delta in range(1, 5))
        destination_value = next(value for value in values if value not in {*picked_up})

        destination_cup = by_value[destination_value]

        cup.next = picked_up[-1].next
        destination_cup.insert(picked_up)

        cup = cup.next

    return by_value[1].next.value * by_value[1].next.next.value


def main():
    print(compute("496138527"))
    # print(compute("389125467"))


if __name__ == "__main__":
    main()
