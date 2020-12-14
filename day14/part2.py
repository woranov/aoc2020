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
    masks = []

    instructions = ((var, val) for var, val in map(lambda s: s.split(" = "), data))

    for var, val in instructions:
        if var == "mask":
            mask = val
            xcount = mask.count("X")

            if xcount:
                masks = []
                # noinspection PyTypeChecker
                for comb in map(iter, itertools.product("01", repeat=xcount)):
                    new_mask = ""
                    for mbit in mask:
                        if mbit == "X":
                            new_mask += next(comb)
                        elif mbit == "1":
                            new_mask += mbit
                        else:  # 0 is treated like X (leaving address unchanged)
                            new_mask += "X"
                    masks.append(new_mask)
            else:
                masks = [mask]

        elif var.startswith("mem"):
            _, _, numaddr = var.rstrip("]").partition("[")
            _, _, addr = bin(int(numaddr)).partition("b")
            _, _, bits = bin(int(val)).partition("b")

            for mask in masks:
                new_addr = ""

                for addr_bit, mask_bit in zip(addr.zfill(36), mask):
                    if mask_bit == "X":
                        new_addr += addr_bit
                    else:
                        new_addr += mask_bit

                mem[new_addr] = bits

    return sum(int("".join(bits), 2) for bits in mem.values())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
