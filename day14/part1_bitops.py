_TESTCASE = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip().splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    165
    """
    mem = {}
    mask = None

    instructions = map(lambda s: s.split(" = "), data)

    for var, val in instructions:
        if var == "mask":
            mask = val
        elif var.startswith("mem"):
            _, _, addr = var.rstrip("]").partition("[")

            mask_passthrough = int(mask.replace("X", "0"), 2)
            mask_overwrite = int(mask.replace("X", "1"), 2)

            mem[int(addr)] = (int(val) | mask_passthrough) & mask_overwrite

    return sum(mem.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
