_TESTCASE = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


def compute(data):
    """
    >>> compute(_TESTCASE)
    71
    """
    head, _, tickets = data.partition("\n\nyour ticket:\n")
    my_ticket, _, nearby_tickets = tickets.partition("\n\nnearby tickets:\n")

    rules = []
    for rule in head.splitlines():
        _, _, ranges = rule.partition(": ")
        ruleset = []
        for lo, hi in (rng.split("-") for rng in ranges.split(" or ")):
            ruleset.append(range(int(lo), int(hi) + 1))
        rules.append(ruleset)

    invalid = 0
    for nearby in nearby_tickets.splitlines():
        fields = map(int, nearby.split(","))
        invalid += sum(
            filter(
                lambda f: not any(f in rng for rule_ in rules for rng in rule_), fields
            )
        )
    return invalid


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
