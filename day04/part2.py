_TESTCASE = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".strip().split(
    "\n\n"
)


# noinspection PyUnboundLocalVariable
def compute(data):
    """
    >>> compute(_TESTCASE)
    4
    """

    def range_checker(lo, hi):
        return lambda x: x.isnumeric() and lo <= int(x) <= hi

    valid_per_unit_hgt_ranges = {"cm": range(150, 194), "in": range(59, 77)}
    valid_hexdigits = frozenset("0123456789abcdef")
    valid_eyecolors = frozenset(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))

    rules = {
        "byr": range_checker(1920, 2002),
        "iyr": range_checker(2010, 2020),
        "eyr": range_checker(2020, 2030),
        "hgt": lambda x: (
            (unit := x[-2:]) in valid_per_unit_hgt_ranges
            and (num_s := x[:-2]).isnumeric()
            and int(num_s) in valid_per_unit_hgt_ranges[unit]
        ),
        "hcl": lambda x: (
            x.startswith("#") and len(hexnum_s := x[1:]) == 6 and set(hexnum_s) <= valid_hexdigits
        ),
        "ecl": lambda x: x in valid_eyecolors,
        "pid": lambda x: x.isnumeric() and len(x) == 9,
    }
    required = frozenset(rules)
    passports = (
        dict(field.split(":") for line in block.splitlines() for field in line.split(" "))
        for block in data
    )

    return sum(
        1
        for passport in passports
        if required <= passport.keys()
        if all(rules[key](val) for key, val in passport.items() if key in rules)
    )


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().split("\n\n")))


if __name__ == "__main__":
    main()
