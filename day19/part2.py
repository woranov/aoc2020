import re
from pprint import pprint

_TESTCASE = """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".strip()


def compute(data):
    """
    >>> compute(_TESTCASE)
    12
    """
    rules_s, _, messages_s = data.partition("\n\n")

    rules = {}

    for rule_s in sorted(rules_s.splitlines()):
        rule_n, _, rule = rule_s.partition(": ")
        rule_n = int(rule_n)
        if '"' in rule:
            rules[rule_n] = rule[1]
        elif rule_n == 8:
            rules[rule_n] = "42 | 42 8"
        elif rule_n == 11:
            rules[rule_n] = "42 31 | 42 11 31"
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

    for rule_n, rule in tuple(rules.items()):
        if rule_n != 0 and str(rule_n) in rule:
            before, _, after = rule.partition(str(rule_n))

            if bool(before) ^ bool(after):
                rules[rule_n] = new_rule = f"({before or after})+"
            else:
                components = []
                for n in range(1, 10):
                    components.append(f"{before}{{{n}}}{after}{{{n}}}")

                rules[rule_n] = new_rule = f"({'|'.join(components)})"

            rules[0] = re.sub(rf"\b{rule_n}\b", new_rule, rules[0])

    pat = re.compile(rules[0].replace(" ", ""))

    return sum(pat.fullmatch(message) is not None for message in messages_s.splitlines())


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        pprint(compute(f.read().strip()))


if __name__ == "__main__":
    main()
