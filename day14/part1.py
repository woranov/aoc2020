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

    instructions = ((var, val) for var, val in map(lambda s: s.split(" = "), data))

    for var, val in instructions:
        if var == "mask":
            mask = val
        elif var.startswith("mem"):
            _, _, addr = var.rstrip("]").partition("[")
            _, _, bits = bin(int(val)).partition("b")

            new_bits = ""

            for bit, mask_bit in zip(bits.zfill(36), mask):
                if mask_bit == "X":
                    new_bits += bit
                else:
                    new_bits += mask_bit

            mem[addr] = new_bits

    return sum(int(bits, 2) for bits in mem.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
