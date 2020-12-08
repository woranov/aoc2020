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
    5
    """
    visited = set()
    acc = 0
    row = 0

    while row not in visited:
        visited.add(row)

        op, num_s = data[row].split()
        num = int(num_s)

        if op == "nop":
            row += 1
        elif op == "acc":
            acc += num
            row += 1
        elif op == "jmp":
            row += num

    return acc


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().splitlines()))


if __name__ == "__main__":
    main()
