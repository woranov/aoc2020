import functools

_TESTCASE = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    8
    """

    # noinspection PyUnboundLocalVariable
    def execute(ops, acc, row, visited, switched=False):
        visited = set(visited)

        while row < len(data):
            if row in visited:
                return None
            else:
                visited.add(row)

            op, num = ops[row]
            switch = functools.partial(
                execute, ops=ops, acc=acc, visited=visited, switched=True
            )

            if op == "acc":
                acc += num
                row += 1
            elif op == "nop":
                if not switched and (alternate := switch(row=row + num)):
                    return alternate
                else:
                    row += 1
            elif op == "jmp":
                if not switched and (alternate := switch(row=row + 1)):
                    return alternate
                else:
                    row += num

        return acc

    return execute(
        ops=[(op, int(num_s)) for op, num_s in map(str.split, data)],
        acc=0,
        row=0,
        visited=set(),
    )


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
