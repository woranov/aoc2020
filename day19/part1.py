import re
from pprint import pprint

_TESTCASE = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip()


def compute(data):
    """
    >>> compute(_TESTCASE)
    2
    """
    rules_s, _, messages_s = data.partition("\n\n")

    rules = {}

    for rule_s in sorted(rules_s.splitlines()):
        rule_n, _, rule = rule_s.partition(": ")
        rule_n = int(rule_n)
        if '"' in rule:
            rules[rule_n] = rule[1]
        else:
            rules[rule_n] = rule

    while True:
        try:
            term_n, term_s = next(
                (rn, rs) for rn, rs in rules.items() if rn != 0 if not any(s.isdigit() for s in rs)
            )
            if "|" in term_s:
                term_s = f"({term_s})"
        except StopIteration:
            break
        else:
            for rule_n, rule_s in tuple(rules.items()):
                if rule_n == term_n:
                    continue
                rules[rule_n] = re.sub(rf"\b{term_n}\b", term_s, rule_s)
            del rules[term_n]

    pat = re.compile(rules[0].replace(" ", ""))

    return sum(pat.fullmatch(message) is not None for message in messages_s.splitlines())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        pprint(compute(f.read().strip()))


if __name__ == "__main__":
    main()
