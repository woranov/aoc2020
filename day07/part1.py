import collections
import re
from typing import NamedTuple

_TESTCASE = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".splitlines()


class BagParent(NamedTuple):
    bag: str
    count: int


LINE_PAT = re.compile(r"([\s\w]+) bags? contain (.+$)")
CONTAIN_PAT = re.compile(r"(\d+) ([\s\w]+) bags?[,.]")


def compute(data):
    """
    >>> compute(_TESTCASE)
    4
    """
    rules = collections.defaultdict(list)

    for match in map(LINE_PAT.match, data):
        bag, contain = match.groups()
        for contains_match in CONTAIN_PAT.finditer(contain):
            count, child = contains_match.groups()
            rules[child].append(BagParent(bag=bag, count=int(count)))

    found_parents = set()
    bag_parents = rules["shiny gold"]

    while bag_parents:
        parent_bag = bag_parents.pop().bag
        if parent_bag not in found_parents:
            found_parents.add(parent_bag)
            bag_parents.extend(rules[parent_bag])

    return len(found_parents)


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
