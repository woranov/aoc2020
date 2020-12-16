import collections
import functools


def compute(data):
    head, _, all_tickets = data.partition("\n\nyour ticket:\n")
    my_ticket, _, nearby = all_tickets.partition("\n\nnearby tickets:\n")

    # abusing comprehensions for no reason

    rules = {
        name: {
            range(int(lo), int(hi) + 1)
            for lo, hi in (rng.split("-") for rng in ranges.split(" or "))
        }
        for name, _, ranges in (line.partition(": ") for line in head.splitlines())
    }

    n = len(rules)

    nearby = {
        fields
        for fields in (
            tuple(map(int, nearby.split(","))) for nearby in nearby.splitlines()
        )
        if not any(
            all(f not in rng for ruleset in rules.values() for rng in ruleset)
            for f in fields
        )
    }

    my_ticket = [*map(int, my_ticket.split(","))]

    columns = {i: {fields[i] for fields in nearby} for i in range(n)}

    column_candidates = collections.defaultdict(set)
    column_mapping = {}

    for rule_name, ruleset in rules.items():
        for column, values in columns.items():
            if all(any(v in rng for rng in ruleset) for v in values):
                column_candidates[rule_name].add(column)

    while column_candidates:
        rule_name, candidates = next(
            (rule_name, candidates)
            for rule_name, candidates in column_candidates.items()
            if len(candidates) == 1
        )
        column_mapping[rule_name] = candidate = column_candidates.pop(rule_name).pop()
        for other in column_candidates.values():
            other.discard(candidate)

    assert len(column_mapping) == n

    return functools.reduce(
        lambda a, b: a * b,
        (
            my_ticket[column]
            for rule_name, column in column_mapping.items()
            if rule_name.startswith("departure")
        ),
    )


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
