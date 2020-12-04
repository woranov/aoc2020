_TESTCASE = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip().split(
    "\n\n"
)


def compute(data):
    """
    >>> compute(_TESTCASE)
    2
    """
    required = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    return sum(
        required
        <= {
            field.split(":")[0]
            for line in block.splitlines()
            for field in line.split(" ")
        }
        for block in data
    )


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().split("\n\n")))


if __name__ == "__main__":
    main()
