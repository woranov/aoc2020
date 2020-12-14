import itertools

_TESTCASE = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip().splitlines()


def compute(data):
    """
    >>> compute(_TESTCASE)
    208
    """
    mem = {}
    mask = None

    instructions = map(lambda s: s.split(" = "), data)

    for var, val in instructions:
        if var == "mask":
            mask = val
        elif var.startswith("mem"):
            _, _, addr = var.rstrip("]").partition("[")

            mask_passthrough = int(mask.replace("X", "1"), 2)
            addr = int(addr) | mask_passthrough

            # noinspection PyTypeChecker
            for comb in map(iter, itertools.product("01", repeat=mask.count("X"))):
                mask_overwrite = int(
                    "".join(
                        next(comb) if bit == "X" else bit
                        for bit in mask.replace("0", "1")
                    ),
                    2,
                )
                mem[addr & mask_overwrite] = int(val)

    return sum(mem.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
