import collections
import re
from typing import NamedTuple

_TESTCASE = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".splitlines()


class BagChild(NamedTuple):
    bag: str
    count: int


LINE_PAT = re.compile(r"([\s\w]+) bags? contain (.+$)")
CONTAIN_PAT = re.compile(r"(\d+) ([\s\w]+) bags?[,.]")


def compute(data):
    """
    >>> compute(_TESTCASE)
    126
    """
    rules = collections.defaultdict(list)

    for match in map(LINE_PAT.match, data):
        bag, contain = match.groups()
        for contains_match in CONTAIN_PAT.finditer(contain):
            count, child = contains_match.groups()
            rules[bag].append(BagChild(bag=child, count=int(count)))

    def total(children):
        return 1 + sum(
            child_count * total(rules[child_bag]) for child_bag, child_count in children
        )

    return total(rules["shiny gold"]) - 1


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
